// 取得頁面訊息
// https://stackoverflow.com/questions/247483/http-get-request-in-javascript
function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false); // false for synchronous request
  xmlHttp.send(null);
  return xmlHttp.responseText;
}
// const http = new XMLHttpRequest();
// http.open(
//   "GET",
//   "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
// );
// http.send();

// http.onload = () => console.log(http.responseText);

var rsp = httpGet(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
);
var cur_index = 0;
var rawData = JSON.parse(rsp);
var location_info_lst = rawData.result.results;
var locations = location_info_lst.length;

// http.onload = function () {
//   rawData = JSON.parse(http.responseText);
//   location_info_lst = rawData.result.results;
//   locations = location_info_lst.length;
// };

//------------------------------------------------------------------------------------------------
function getFirstFigUrl(index) {
  //   console.log("https" + location_info_lst[index].file.split("https")[1]);
  fig_url = location_info_lst[index].file.split("https")[1];
  res = "https" + fig_url;
  return res;
}
function getLocationName(index) {
  //   console.log(location_info_lst[index].stitle);
  return location_info_lst[index].stitle;
}

function createBoxes(index) {
  let boundIndex = index + 8;
  if (index > locations) {
    return;
  } else if (boundIndex >= locations) {
    boundIndex = locations - 1;
  }
  let figsContainer = document.getElementById("boxesContainer");

  // 建立一個 DocumentFragment，可以把它看作一個「虛擬的容器」
  var fragment = document.createDocumentFragment();

  for (let i = index; i < boundIndex; i++) {
    let box = document.createElement("div");
    box.className = "box";
    let picture = document.createElement("img");
    picture.src = getFirstFigUrl(i);

    picture.className = "picture";
    let title = document.createElement("div");
    title.className = "title";
    title.appendChild(document.createTextNode("" + getLocationName(i)));
    box.appendChild(picture);
    box.appendChild(title);
    fragment.appendChild(box);
  }
  figsContainer.appendChild(fragment);
  cur_index = boundIndex;
}
function insertBoxes() {
  let index = cur_index;
  createBoxes(index);
}

function main() {
  console.log(locations);
  createBoxes(0);
  let btn = document.getElementById("btn");
  btn.onclick = insertBoxes;
}

window.onload = main;
