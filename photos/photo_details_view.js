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

    leftArrow.addEventListener("click", () => {
      this.currentIndex--;
    });

    right.addEventListener("click", () => {
      this.currentIndex++;
    });
  },
  display(tag, photos, index) {
    this.currentTag = tag;
    this.currentPhotos = photos;
    this.currentIndex = index;
    modal.style.display = "block";
  },
  hide() {
    modal.style.display = "none";
  },
  _setOriginalPhoto() {
    let photos = this.currentPhotos;
    let i = this.currentIndex;
    originalPhoto.setAttribute("src", `resources/${this.currentTag}/${photos[i].name}-raw.jpg`);

    let dateFormat = { year: 'numeric', month: 'long', day: 'numeric' };
    document.querySelector("#date").textContent = new Date(photos[i].date).toLocaleDateString("en-US", dateFormat);
    document.querySelector("#location").textContent = photos[i].location;
  },
  _displayArrows(index) {
    leftArrow.style.display = index === 0 ? "none" : "block";
    rightArrow.style.display = index === (this.thumbnailNum - 1) ? "none" : "block";
  }
};
