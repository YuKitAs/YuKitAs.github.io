var photoDetailsView = {
  thumbnailNum: 0,
  currentTag: "",
  currentPhotos: [],
  _currentIndex: 0,
  get currentIndex() {
    return this._currentIndex;
  },
  set currentIndex(index) {
    this._currentIndex = index;
    this._setOriginalPhoto();
    this._displayArrows(index);
  },
  addEventListenerOnLoad(thumbnailNum) {
    this.thumbnailNum = thumbnailNum;

    document.querySelector("#left").onclick = () => this.currentIndex--;
    document.querySelector("#right").onclick = () => this.currentIndex++;

    document.onkeydown = e => {
      if (this.currentIndex !== 0 && e.key === "ArrowLeft" || e.key === "Left") {
        this.currentIndex--;
        return;
      }

      if (this.currentIndex !== (this.thumbnailNum - 1) && e.key === "ArrowRight" || e.key === "Right") {
        this.currentIndex++;
        return;
      }

      if (e.key === "Escape") {
        this.hide();
      }
    };
  },
  display(tag, photos, index) {
    this.currentTag = tag;
    this.currentPhotos = photos;
    this.currentIndex = index;
    document.querySelector("#modal").style.display = "block";
  },
  hide() {
    document.querySelector("#modal").style.display = "none";
  },
  _setOriginalPhoto() {
    let photos = this.currentPhotos;
    let i = this.currentIndex;
    document.querySelector("#original-photo").setAttribute("src", `resources/${this.currentTag}/${photos[i].name}-raw.jpg`);

    let dateFormat = { year: 'numeric', month: 'long', day: 'numeric' };
    document.querySelector("#date").textContent = new Date(photos[i].date).toLocaleDateString("en-US", dateFormat);
    document.querySelector("#location").textContent = photos[i].location;
  },
  _displayArrows(index) {
    document.querySelector("#left").style.display = index === 0 ? "none" : "block";
    document.querySelector("#right").style.display = index === (this.thumbnailNum - 1) ? "none" : "block";
  }
};
