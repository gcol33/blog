# Inline Blog Post Editor

Browser-based markdown editor for editing blog posts directly on the site without local workflow.

## Features

- Edit any published post directly in the browser
- Markdown editor with live preview (SimpleMDE)
- Commits changes directly to GitHub via API
- Authentication via GitHub Personal Access Token
- Only visible to authenticated admin (you)
- No changes to existing blog workflow required

## Setup

### 1. Create GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a descriptive name: "Blog Inline Editor"
4. Set expiration (recommend 90 days or longer)
5. Select scope: **`repo`** (full control of private repositories)
6. Click "Generate token"
7. **IMPORTANT**: Copy the token immediately (you won't see it again)

### 2. Using the Editor

#### First Time Setup

1. Visit any blog post on your published site
2. Look for "Admin Login" link at the top of the post
3. Click it and paste your GitHub Personal Access Token
4. Token is stored in browser localStorage (persists across sessions)

#### Editing Posts

1. Once authenticated, you'll see "Edit Post" and "Logout" buttons at the top
2. Click "Edit Post" to open the markdown editor
3. Make your changes in the editor
4. Optionally add a commit message
5. Click "Save Changes"
6. Wait ~30 seconds for GitHub Pages to rebuild
7. Refresh to see your changes

#### Logging Out

Click "Logout" to remove the stored token from your browser.

## Files Added

```
assets/
├── js/
│   └── inline-editor.js    # Editor logic, GitHub API, authentication
└── css/
    └── inline-editor.css   # Modal and button styles

_layouts/
└── default.html           # Modified to include editor scripts on post pages
```

## Security Notes

- Token is stored in browser localStorage (client-side only)
- Token is never committed to the repository
- Token is never sent anywhere except GitHub API
- Only works with `repo` scope token
- Editor only appears when authenticated
- Clear token from browser by clicking "Logout" or clearing localStorage

## Troubleshooting

### "Could not determine post filename"
- Post must have valid front matter with `title` and `date`
- Post must be in `_posts/` directory with format `YYYY-MM-DD-slug.md`

### "GitHub API error: 401"
- Token expired or invalid
- Token doesn't have `repo` scope
- Click "Logout" and re-authenticate with a new token

### "GitHub API error: 404"
- File path couldn't be found
- Check that the post filename matches the expected format
- Verify repo name is `gcol33/blog`

### Changes don't appear
- GitHub Pages takes 30-60 seconds to rebuild
- Check the Actions tab on GitHub to see build status
- Hard refresh the page (Ctrl+Shift+R or Cmd+Shift+R)

### Editor doesn't show
- Make sure you're on a post page (not home, archives, etc.)
- Check browser console for JavaScript errors
- Verify SimpleMDE loaded from CDN

## Removing the Editor

To remove the inline editor completely:

1. Delete `assets/js/inline-editor.js`
2. Delete `assets/css/inline-editor.css`
3. Remove these lines from `_layouts/default.html`:
   - SimpleMDE CSS and JS includes (lines 36-39, 165-169)
4. Commit and push changes

## Technical Details

- **SimpleMDE**: Lightweight markdown editor with preview
- **GitHub Contents API**: Used to read/write files
- **Authentication**: GitHub Personal Access Token (classic)
- **Storage**: Browser localStorage for token persistence
- **No backend required**: Pure client-side implementation
