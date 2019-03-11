/* global load initialize */

const scripts = [
  initialize
];

const globalData = {};

const eventBus = document.createElement("div");

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", load(scripts, globalData, eventBus));
} else {
  load(scripts, globalData, eventBus);
}
