function renderHeader() {
  const greeting = `$ echo "${_greet()}, Sekai!"`;
  const nav = `<div class="nav">
                  <a href="/"><span class="nav-item">Home</span></a> |
                  <a href="/photos"><span class="nav-item">Photos</span></a> |
                  <a href="/drawings"><span class="nav-item">Drawings</span></a> |
                  <a href="/about"><span class="nav-item">About</span></a>
                </div>`;
  document.body.innerHTML = `<h1>${greeting}</h1>` + `${nav}` + document.body.innerHTML;
}

function renderHomeImage() {
  document.body.innerHTML += `<img class="home before" id="home-before" src="/assets/images/home-before.png" alt="" />`;
  document.body.innerHTML += `<img class="home after" id="home-after" src="/assets/images/home-after.png" alt="" />`;
}

function renderUpArrow() {
  document.body.innerHTML += `<img class="top-icon" id="top" src="/assets/icons/up-arrow-white.png" onclick="scrollToTop()" />`;
}

function renderFooter() {
  document.body.innerHTML += `<footer>
                                <p>All rights reserved © 2018-2020 YuKitAs</p>
                              </footer>`;
}

function _greet() {
  let hour = new Date().getHours();
  let greet = (hour >= 6 && hour <= 18) ? "Konnichiwa" : "Konbanwa";
  console.log(`🐹: ${greet}, Sekai!`);

  return greet;
}
