(function() {
  'use strict';

  // Configuration
  const GITHUB_API = 'https://api.github.com';
  const REPO_OWNER = 'gcol33';
  const REPO_NAME = 'blog';
  const TOKEN_KEY = 'github_editor_token';

  // Authentication Manager
  const authManager = {
    getToken: function() {
      return localStorage.getItem(TOKEN_KEY);
    },

    setToken: function(token) {
      localStorage.setItem(TOKEN_KEY, token);
    },

    clearToken: function() {
      localStorage.removeItem(TOKEN_KEY);
    },

    checkAuth: async function() {
      const token = this.getToken();
      if (!token) return false;

      try {
        const response = await fetch(`${GITHUB_API}/user`, {
          headers: {
            'Authorization': `token ${token}`,
            'Accept': 'application/vnd.github.v3+json'
          }
        });
        return response.ok;
      } catch (e) {
        return false;
      }
    },

    showAuthPrompt: function() {
      const token = prompt(
        'Enter your GitHub Personal Access Token:\n\n' +
        'This token needs "repo" scope to edit posts.\n' +
        'Create one at: https://github.com/settings/tokens'
      );

      if (token) {
        this.setToken(token.trim());
        location.reload();
      }
    },

    logout: function() {
      if (confirm('Remove stored GitHub token?')) {
        this.clearToken();
        location.reload();
      }
    }
  };

  // GitHub API
  const githubAPI = {
    getFile: async function(path) {
      const token = authManager.getToken();
      const url = `${GITHUB_API}/repos/${REPO_OWNER}/${REPO_NAME}/contents/${path}`;

      const response = await fetch(url, {
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      });

      if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status}`);
      }

      const data = await response.json();
      return {
        content: atob(data.content),
        sha: data.sha
      };
    },

    updateFile: async function(path, content, sha, message) {
      const token = authManager.getToken();
      const url = `${GITHUB_API}/repos/${REPO_OWNER}/${REPO_NAME}/contents/${path}`;

      const response = await fetch(url, {
        method: 'PUT',
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: message,
          content: btoa(unescape(encodeURIComponent(content))),
          sha: sha
        })
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || `GitHub API error: ${response.status}`);
      }

      return await response.json();
    }
  };

  // Editor Manager
  const editorManager = {
    modal: null,
    editor: null,
    currentFile: null,
    currentSha: null,

    init: function() {
      this.createModal();
      this.createEditButton();
    },

    getCurrentFilePath: function() {
      // Extract post filename from page metadata
      const postDate = document.querySelector('.post-date');
      const postTitle = document.querySelector('.post-title');

      if (!postDate || !postTitle) {
        console.error('Could not find post metadata');
        return null;
      }

      // Parse date from post
      const dateText = postDate.textContent.trim();
      const date = new Date(dateText);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');

      // Create slug from title
      const slug = postTitle.textContent
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-');

      return `_posts/${year}-${month}-${day}-${slug}.md`;
    },

    createEditButton: function() {
      const article = document.querySelector('.post');
      if (!article) return;

      const btnContainer = document.createElement('div');
      btnContainer.id = 'inline-editor-controls';
      btnContainer.innerHTML = `
        <button id="edit-post-btn" class="inline-editor-btn">Edit Post</button>
        <button id="logout-btn" class="inline-editor-btn inline-editor-btn-secondary">Logout</button>
      `;

      article.insertBefore(btnContainer, article.firstChild);

      document.getElementById('edit-post-btn').addEventListener('click', () => {
        this.openEditor();
      });

      document.getElementById('logout-btn').addEventListener('click', () => {
        authManager.logout();
      });
    },

    createModal: function() {
      const modal = document.createElement('div');
      modal.id = 'inline-editor-modal';
      modal.innerHTML = `
        <div class="inline-editor-backdrop"></div>
        <div class="inline-editor-container">
          <div class="inline-editor-header">
            <h3>Edit Post</h3>
            <button id="close-editor-btn" class="inline-editor-close">&times;</button>
          </div>
          <div class="inline-editor-body">
            <textarea id="markdown-editor"></textarea>
          </div>
          <div class="inline-editor-footer">
            <input type="text" id="commit-message" placeholder="Commit message (optional)" />
            <div class="inline-editor-actions">
              <button id="cancel-edit-btn" class="inline-editor-btn inline-editor-btn-secondary">Cancel</button>
              <button id="save-edit-btn" class="inline-editor-btn">Save Changes</button>
            </div>
          </div>
          <div id="editor-status" class="inline-editor-status"></div>
        </div>
      `;

      document.body.appendChild(modal);
      this.modal = modal;

      // Event listeners
      document.getElementById('close-editor-btn').addEventListener('click', () => {
        this.closeEditor();
      });

      document.getElementById('cancel-edit-btn').addEventListener('click', () => {
        this.closeEditor();
      });

      document.getElementById('save-edit-btn').addEventListener('click', () => {
        this.saveChanges();
      });

      modal.querySelector('.inline-editor-backdrop').addEventListener('click', () => {
        this.closeEditor();
      });
    },

    showStatus: function(message, isError = false) {
      const status = document.getElementById('editor-status');
      status.textContent = message;
      status.className = 'inline-editor-status ' + (isError ? 'error' : 'success');
      status.style.display = 'block';

      setTimeout(() => {
        status.style.display = 'none';
      }, 5000);
    },

    openEditor: async function() {
      const filePath = this.getCurrentFilePath();
      if (!filePath) {
        alert('Could not determine post filename');
        return;
      }

      this.currentFile = filePath;
      this.modal.style.display = 'block';
      document.body.style.overflow = 'hidden';

      try {
        this.showStatus('Loading post content...');

        const fileData = await githubAPI.getFile(filePath);
        this.currentSha = fileData.sha;

        // Initialize SimpleMDE
        if (!this.editor) {
          this.editor = new SimpleMDE({
            element: document.getElementById('markdown-editor'),
            spellChecker: false,
            status: false,
            toolbar: [
              'bold', 'italic', 'heading', '|',
              'quote', 'unordered-list', 'ordered-list', '|',
              'link', 'image', '|',
              'preview', 'side-by-side', 'fullscreen', '|',
              'guide'
            ]
          });
        }

        this.editor.value(fileData.content);
        this.showStatus('Ready to edit');

      } catch (error) {
        console.error('Error loading file:', error);
        this.showStatus('Error loading file: ' + error.message, true);
      }
    },

    closeEditor: function() {
      if (this.editor && this.editor.value() !== '') {
        if (!confirm('Close editor? Unsaved changes will be lost.')) {
          return;
        }
      }

      this.modal.style.display = 'none';
      document.body.style.overflow = '';

      if (this.editor) {
        this.editor.value('');
      }
    },

    saveChanges: async function() {
      const content = this.editor.value();
      const commitMsgInput = document.getElementById('commit-message');
      const commitMessage = commitMsgInput.value.trim() || 'Update post via inline editor';

      if (!content.trim()) {
        alert('Content cannot be empty');
        return;
      }

      const saveBtn = document.getElementById('save-edit-btn');
      saveBtn.disabled = true;
      saveBtn.textContent = 'Saving...';

      try {
        this.showStatus('Committing changes to GitHub...');

        await githubAPI.updateFile(
          this.currentFile,
          content,
          this.currentSha,
          commitMessage
        );

        this.showStatus('Changes saved successfully!');

        setTimeout(() => {
          this.closeEditor();
          if (confirm('Post updated successfully! Reload page to see changes?')) {
            location.reload();
          }
        }, 1500);

      } catch (error) {
        console.error('Error saving file:', error);
        this.showStatus('Error saving: ' + error.message, true);
      } finally {
        saveBtn.disabled = false;
        saveBtn.textContent = 'Save Changes';
      }
    }
  };

  // Initialize on page load
  document.addEventListener('DOMContentLoaded', async function() {
    // Only run on post pages
    if (!document.querySelector('.post')) return;

    const isAuthenticated = await authManager.checkAuth();

    if (!isAuthenticated) {
      // Show subtle login link
      const article = document.querySelector('.post');
      if (article) {
        const loginLink = document.createElement('div');
        loginLink.id = 'inline-editor-login';
        loginLink.innerHTML = '<a href="#" id="login-link">Admin Login</a>';
        article.insertBefore(loginLink, article.firstChild);

        document.getElementById('login-link').addEventListener('click', (e) => {
          e.preventDefault();
          authManager.showAuthPrompt();
        });
      }
    } else {
      // Authenticated - show editor controls
      editorManager.init();
    }
  });

})();
