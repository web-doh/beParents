"use strict";
import SetScreen from "../../../static/scripts/screen.js";
import Sorting from "../../../static/scripts/sorting.js";
import * as display from "../../../static/scripts/display.js";

const mainScreen = new SetScreen();
const orderedBy = new Sorting();

//  main 화면 높이 설정
const mapSection = document.querySelector("#map__section");
const changeCenterBtn = document.querySelector(".change__map-center");

window.addEventListener("DOMContentLoaded", () => {
  mainScreen.setMainHeight(mapSection);
  alignBtn();
});
window.addEventListener("resize", () => {
  mainScreen.setMainHeight(mapSection);
  changeCenterBtn && alignBtn();
});

// 지도보기 : 현재 지도 위치로 재설정 버튼 align
function alignBtn() {
  const btnWidth = changeCenterBtn.getBoundingClientRect().width;
  const mapWidth = mapSection.getBoundingClientRect().width;
  const btnX = (mapWidth - btnWidth) / 2;

  changeCenterBtn.style.left = btnX + "px";
}

// 목록보기 : arrow 버튼 클릭시 화면 상단으로 이동
mainScreen.setClickListener(() =>
  mainScreen.scrollIntoView(".center__list .center__item")
);

// 보기 타입 변경 (목록보기, 지도보기)
const typeBtn = document.querySelector(".map__type__btn");
const mapType = document.querySelector(".map__container");
const listType = document.querySelector(".list__container");
const typeName = document.querySelector(".type__description");

typeBtn.addEventListener("click", changeDisplayType);

function changeDisplayType() {
  if (mapType.classList.contains("inactive")) {
    display.show(mapType);
    display.hide(listType);
    changeTypeName("목록");
  } else {
    display.show(listType);
    display.hide(mapType);
    changeTypeName("지도");
    mainScreen.scrollIntoView();
  }
}

function changeTypeName(name) {
  typeName.textContent = name;
}

// -- map 기본 설정 --
const mapTag = document.querySelector(".map");

const nearCenters = []; // 가까운 센터 리스트
const markers = []; // 마커 리스트

let userX = 37.5666103; // 위치허용 하지 않을때, 사용자 중심값 : 서울시청
let userY = 126.9783882;

let mapX; // 현재 맵의 중심 좌표
let mapY;

const map = new naver.maps.Map("map", {
  center: new naver.maps.LatLng(userX, userY),
  zoom: 14,
});

// -- ajax로 서버에 현재위치 전달하고, 3km 이내 센터 데이터 받아오기 --
function getData() {
  changeCenter();
  ajaxCommunication(userX, userY, mapX, mapY)
    .then((data) => {
      mainScreen.main.innerHTML = data;
      const centers = document.querySelectorAll(".center__list .center__item");
      successHandler(centers, nearCenters);
    })
    .catch((e) => console.log("error:" + e.status));
}

function changeCenter() {
  mapX = map.getCenter().y;
  mapY = map.getCenter().x;
}

function ajaxCommunication(userX, userY, mapX, mapY) {
  return new Promise(function (resolve, reject) {
    $.ajax({
      type: "POST",
      url: "/map/ajax/",
      dataType: "html",
      data: {
        userX,
        userY,
        mapX,
        mapY,
      },
      success: resolve,
      error: reject,
    });
  });
}

// 데이터 받아오기 성공시,
function successHandler(data, list) {
  getCenterList(data, list);
  setMarkers(list);
}

// 1. html 데이터 Array로 변환해서 가져오기
function getCenterList(data, list) {
  if (list.length) {
    list.length = 0;
  }

  data.forEach((datum) => {
    const id = datum.id;
    const distanceData = getText(datum, ".center__distance");
    const addressData = getText(datum, ".center__address");

    const distance = setDistance(distanceData);
    const address = setAddress(addressData);

    // html 내 데이터 수정 (거리, 주소 )
    setText(datum, ".center__distance", distance);
    setText(datum, ".center__address", address);

    const center = {
      id,
      name: getText(datum, ".center__name"),
      distance,
      address,
      average: getText(datum, ".center__average"),
      counts: getText(datum, ".center__counts"),
      type: getText(datum, ".center__type"),
      x: getText(datum, "#centerX"),
      y: getText(datum, "#centerY"),
    };

    list.push(center);
  });
}

// html 태그의 내용 가져오기
function getText(parent, selector) {
  const text = parent.querySelector(selector).innerHTML;
  return text;
}

// html 태그 안에 내용 넣기
function setText(parent, selector, text) {
  const tag = parent.querySelector(selector);
  tag.textContent = text;
}

// 주소 요약 하기
function setAddress(address) {
  const longAddress = address.split(" ");
  const shortAddress = `${longAddress[0]} ${longAddress[1] || ""} ${
    longAddress[2] || ""
  } `;
  return shortAddress;
}

// 거리 단위 설정
function setDistance(distance) {
  if (distance < 1) {
    distance = `${distance * 1000}m`;
  } else {
    distance = `${Math.round(distance * 10) / 10}km`;
  }
  return distance;
}

// 현재 위치 허용하면, 서버에서 데이터 다시 받아오기
const locationNowBtn = document.querySelector(".location-now__btn");

window.addEventListener("DOMContentLoaded", () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      onSuccessLocation,
      onErrorGeolocation
    );
  } else {
    alert("GPS를 지원하지 않습니다.");
    getData();
  }
});

locationNowBtn.addEventListener("click", () => {
  if (!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(
    onSuccessLocation,
    onErrorGeolocation
  );
});

function onSuccessLocation(position) {
  let location = new naver.maps.LatLng(
    position.coords.latitude,
    position.coords.longitude
  );
  map.setCenter(location);

  userX = position.coords.latitude;
  userY = position.coords.longitude;

  showCurrentMarker(location);
  getData();
}

// 현재위치 마커 설정 (위치 허용시)
function showCurrentMarker(position) {
  let currentMarker = document.querySelector(
    'img[src="../static/map/image/current.png"]'
  );
  if (currentMarker) return;
  const markerOptions = {
    position,
    map,
    icon: {
      url: "../static/map/image/current.png",
      size: new naver.maps.Size(36, 36),
      origin: new naver.maps.Point(0, 0),
      anchor: new naver.maps.Point(0, 0),
    },
  };
  currentMarker = new naver.maps.Marker(markerOptions);
  return currentMarker;
}

function onErrorGeolocation() {
  alert("설정에서 위치 접근 권한을 허용해 주세요.");
  getData();
}

// 현 지도에서 검색하기 버튼 클릭시, 주변 센터 리스트 재요청
naver.maps.Event.addListener(map, "center_changed", () => {
  display.show(changeCenterBtn);
});

changeCenterBtn.addEventListener("click", () => {
  display.hide(changeCenterBtn);
  getData();
});

//-- marker 설정 --
function setMarkers(list) {
  // 기존 마커 삭제
  if (markers.length) {
    markers.forEach((marker) => hideMarker(map, marker));
    markers.length = 0;
  }

  // 새로운 마커 등록
  list.forEach((center) => {
    const name = center["name"];
    const position = new naver.maps.LatLng(center["x"], center["y"]);
    const marker = showMarkers(position, name);
    markers.push(marker);
  });
}

// 일반 마커 설정
const markerUrl = "../static/map/image/marker.png";
const selectedUrl = "../static/map/image/big-marker.png";
const markerSize = new naver.maps.Size(36, 36);
const selectedSize = new naver.maps.Size(42, 42);
const markerOffset = new naver.maps.Point(27, 12);
const selectedOffset = new naver.maps.Point(32, 36);

let selectedMarker = null;

const normalIcon = createMarkerIcon(markerUrl, markerSize, markerOffset);
const selectedIcon = createMarkerIcon(
  selectedUrl,
  selectedSize,
  selectedOffset
);

function showMarkers(position, name) {
  const marker = new naver.maps.Marker({
    map,
    position,
    title: name,
    icon: normalIcon,
    zindex: 100,
  });

  marker.normalIcon = normalIcon;
  naver.maps.Event.addListener(marker, "click", getClickHandler);

  return marker;
}

function createMarkerIcon(url, markerSize, offset) {
  let markerIcon = {
    url,
    size: markerSize,
    origin: new naver.maps.Point(0, 0),
    anchor: offset,
  };
  return markerIcon;
}

// 화면에서 벗어난 마커 숨기기
naver.maps.Event.addListener(map, "idle", function () {
  updateMarkers(map, markers);
});

function updateMarkers(map, markers) {
  const mapBounds = map.getBounds();
  let marker;
  let position;

  for (let i = 0; i < markers.length; i++) {
    marker = markers[i];
    position = marker.getPosition();

    if (mapBounds.hasLatLng(position)) {
      showMarker(map, marker);
    } else {
      hideMarker(map, marker);
    }
  }
}

function showMarker(map, marker) {
  if (marker.setMap()) return;
  marker.setMap(map);
}

function hideMarker(map, marker) {
  if (!marker.setMap()) return;
  marker.setMap(null);
}

// -- 마커 클릭 이벤트 --
function getClickHandler(e) {
  const target = e.overlay;
  showSummary(target);
  showSelectedMarker(target);
}

// 1. summary 창 오픈
const centerSummary = document.querySelector("#center__summary");

function showSummary(e) {
  getSummary(e);
  mapTag.style.height = "calc(100% - 10.5rem)";
  display.show(centerSummary);
}

function hideSummary() {
  display.hide(centerSummary);
  mapTag.style.height = "100%";
}

function getSummary(e) {
  const target = e.title;
  const targetIndex = nearCenters.findIndex((obj) => obj.name == target);
  const summary = document.querySelector("#center__summary");

  const center = nearCenters[targetIndex];
  const { id, name, distance, address, type } = center;
  const counts = center["counts"] || 0;
  const average = center["average"] || 0.0;

  setTagAttribute(".center__name", "href", `/centers/${id}`);

  for (let key in center) {
    if (key == "id" || key == "x" || key == "y") continue;
    setText(summary, `.center__${key}`, center[key]);
  }
}

// html 태그 속성 변경
function setTagAttribute(selector, attribute, value) {
  const target = document.querySelector(selector);
  target.setAttribute(attribute, value);
}

//2. 선택된 마커 사이즈 확대
function showSelectedMarker(marker) {
  if (!selectedMarker || selectedMarker !== marker) {
    !!selectedMarker && selectedMarker.setIcon(normalIcon);
    marker.setIcon(selectedIcon);
    selectedMarker = marker;
  } else if (!selectedMarker || selectedMarker == marker) {
    marker.setIcon(normalIcon);
    selectedMarker = null;
    hideSummary();
  }
}
