#!/bin/bash

cat <<_EOF_
<!DOCTYPE html>
<html lang='en'>

<head>
  <meta charset='UTF-8' />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="msapplication-TileColor" content="#da532c">
  <meta name="theme-color" content="#ffffff">
  <link rel="stylesheet" href="/assets/css/styles.css">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16x16.png">
  <link rel="mask-icon" href="/assets/icons/safari-pinned-tab.svg" color="#5bbad5">
  <link rel="manifest" href="/site.webmanifest">
  <script src="/js/initialize.js"></script>
  <script src="/js/data_loader.js"></script>
  <script src="/js/utils.js"></script>
  <script src="photo_details_view.js"></script>
  <title id="title"></title>
</head>

<body>
  <style scoped>
    /* Mobile phones: 1 col */
    @media only screen and (max-width: 768px) {
      .container {
        width: 250px;
      }

      .photo-details {
        display: inline-block;
        text-align: center;
      }

      .close-button {
        margin: auto;
      }

      .photo-overlay {
        flex-direction: column;
      }

      .original-photo {
        width: 80vw;
        height: auto;
      }
    }

    /* Tablets: 2 cols */
    @media only screen and (min-width: 768px) {
      .container {
        width: 512px;
      }
    }

    /* PC: 4 cols */
    @media only screen and (min-width: 1200px) {
      .container {
        width: 1024px;
      }
    }
  </style>

  <div class="container">
    <div class="description" id="description"></div>
    <div class="thumbnails" id="$NAME"></div>
  </div>

  <div class="modal" id="modal">
    <div class="photo-details" id="photo-details">
      <div class="photo-container">
        <img class="original-photo" id="original-photo" />
        <div class="photo-overlay">
          <div class="date" id="date"></div>
          <div class="location" id="location"></div>
        </div>
      </div>
      <div class="close-button" onclick="photoDetailsView.hide()">
        <svg width="32px" height="32px" enable-background="new 0 0 32 32" viewBox="0 0 512 512" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <path class="close-icon" d="M256,33C132.3,33,32,133.3,32,257c0,123.7,100.3,224,224,224c123.7,0,224-100.3,224-224C480,133.3,379.7,33,256,33z    M364.3,332.5c1.5,1.5,2.3,3.5,2.3,5.6c0,2.1-0.8,4.2-2.3,5.6l-21.6,21.7c-1.6,1.6-3.6,2.3-5.6,2.3c-2,0-4.1-0.8-5.6-2.3L256,289.8   l-75.4,75.7c-1.5,1.6-3.6,2.3-5.6,2.3c-2,0-4.1-0.8-5.6-2.3l-21.6-21.7c-1.5-1.5-2.3-3.5-2.3-5.6c0-2.1,0.8-4.2,2.3-5.6l75.7-76   l-75.9-75c-3.1-3.1-3.1-8.2,0-11.3l21.6-21.7c1.5-1.5,3.5-2.3,5.6-2.3c2.1,0,4.1,0.8,5.6,2.3l75.7,74.7l75.7-74.7   c1.5-1.5,3.5-2.3,5.6-2.3c2.1,0,4.1,0.8,5.6,2.3l21.6,21.7c3.1,3.1,3.1,8.2,0,11.3l-75.9,75L364.3,332.5z" />
        </svg>
      </div>
    </div>

    <img class="arrow left" id="left" src="/assets/icons/left-arrow.svg" />
    <img class="arrow right" id="right" src="/assets/icons/right-arrow.svg" />
  </div>

  <script>
    var tag = "$NAME";

    document.getElementById("title").textContent = tag.charAt(0).toUpperCase() + tag.slice(1) + " - YuKitAs";

    window.onload = () => {
      renderHeader();
      renderFooter();

      dataLoader.load("photos").then(metadata => {
        let content = JSON.parse(metadata).content
        let photosInfo = JSON.parse(b64DecodeUnicode(content)).data.find(photosByTag => photosByTag.name === tag)

        document.getElementById("description").innerHTML = photosInfo.description;

        const photos = photosInfo.photos.reverse();
        let thumbnailNum = photos.length;
        photoDetailsView.addEventListenerOnLoad(thumbnailNum);

        for (let i = 0; i < thumbnailNum; i++) {
          let card = document.createElement("span");
          card.setAttribute("class", "thumbnail-card");

          let zoomIcon = document.createElement("img");
          zoomIcon.setAttribute("class", "zoom-icon");
          zoomIcon.setAttribute("src", "/assets/icons/zoom.png");

          let thumbnailDOM = document.createElement("img");
          thumbnailDOM.setAttribute("class", "thumbnail");
          let thumbnailName = \`resources/\${tag}/\${photos[i].name}-thumbnail\`;
          thumbnailDOM.setAttribute("src", thumbnailName + ".jpg");
          thumbnailDOM.onclick = () => photoDetailsView.display(tag, photos, i);

          card.append(zoomIcon);
          card.append(thumbnailDOM);
          document.getElementById(tag).appendChild(card);
        }
      });
    };

    window.onclick = e => {
      if (e.target === modal) {
        e.preventDefault();
        e.stopPropagation();
        photoDetailsView.hide();
      }
    };
  </script>
</body>

</html>

_EOF_
