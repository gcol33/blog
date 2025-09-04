source "https://rubygems.org"

# Core
gem "jekyll", "~> 4.4.1"
gem "webrick", "~> 1.8"   # needed for `jekyll serve` on Ruby 3+
gem "logger"              # silences the Ruby 3.4 logger warning

# Plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows / JRuby platforms (updated syntax)
platforms :windows, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# File watching on Windows
gem "wdm", "~> 0.1", platforms: [:windows]
