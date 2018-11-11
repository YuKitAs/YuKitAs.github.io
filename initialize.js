function init() {
  this._initHead();
  this._renderHeader();
}

function _initHead() {
  let title = "Erleuchtung - YuKitAs";
  document.head.innerHTML =
      '<meta charset="UTF-8"/> \
      <meta name="viewport" content="width=device-width, initial-scale=1"/> \
      <meta name="msapplication-TileColor" content="#da532c"> \
      <meta name="theme-color" content="#ffffff"> \
      <link rel="stylesheet" href="/assets/css/styles.css"> \
      <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png"> \
      <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png"> \
      <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16x16.png"> \
      <link rel="mask-icon" href="/assets/icons/safari-pinned-tab.svg" color="#5bbad5"> \
      <link rel="manifest" href="/site.webmanifest">' +
      `<title>${title}</title>`;
}

function _renderHeader() {
  let greeting = "Konnichiwa Sekai!";
  let nav = '<div class="nav"> \
                <a href="/"><span class="nav-item">Home</span></a> | \
                <a href="/photos"><span class="nav-item">Photos</span></a> | \
                <a href="/drawings"><span class="nav-item">Drawings</span></a> | \
                <a href="/about"><span class="nav-item">About</span></a> \
              </div>';
  document.body.innerHTML = `<h1>${greeting}</h1>` + `${nav}` + document.body.innerHTML;
}
