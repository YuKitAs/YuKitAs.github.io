function load(name) {
  const url = `https://raw.githubusercontent.com/YuKitAs/YuKitAs.github.io/master/photos/resources/${name}/metadata.json`;

  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.timeout = 3000;
    xhr.onload = () => {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          resolve(xhr.responseText);
        } else {
          reject(xhr.statusText);
        }
      }
    };
    xhr.ontimeout = () => {
      reject("Timeout");
    };
    xhr.open("GET", url, true);
    xhr.send();
  });
}