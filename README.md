# YuKitAs.github.io

1. Install dependencies:

  ```console
  $ bundle install
  $ npm install
  ```

2. Build and serve with Jekyll:

  ```console
  $ bundle exec jekyll serve
  ```

3. Visit `http://localhost:4000`

Tested on Chrome 69, Firefox 62, Safari 12.

### Troubleshooting

* For `FATAL: Listen error: unable to monitor directories for changes`, run the following config and retry ([more info](https://github.com/guard/listen/wiki/Increasing-the-amount-of-inotify-watchers)):

  ```console
  $ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
  ```
