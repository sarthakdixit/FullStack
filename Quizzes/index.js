let constraintObj = { 
  audio: true, 
  video: { 
      facingMode: "user", 
      width: 500,
      height: 300 
  } 
};

var error = false;
var chance = 6;
var active = true;
var isTestStarted = false;
var database = "aptitude";
var que_id = [];
let time = 20;

document.getElementById("min").innerHTML = time;

while(que_id.length < 5){
    var r = Math.floor(Math.random() * 10) + 1;
    if(que_id.indexOf(r) === -1) que_id.push(r);
}
console.log(que_id);

//handle older browsers that might implement getUserMedia in some way
if (navigator.mediaDevices === undefined) {
  navigator.mediaDevices = {};
  navigator.mediaDevices.getUserMedia = function(constraintObj) {
      let getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
      if (!getUserMedia) {
          return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
      }
      return new Promise(function(resolve, reject) {
          getUserMedia.call(navigator, constraintObj, resolve, reject);
      });
  }
}else{
  navigator.mediaDevices.enumerateDevices()
  .then(devices => {
      devices.forEach(device=>{
          console.log(device.kind.toUpperCase(), device.label);
          //, device.deviceId
      })
  })
  .catch(err=>{
      console.log(err.name, err.message);
  })
}

navigator.mediaDevices.getUserMedia(constraintObj)
.then(function(mediaStreamObj) {
  //connect the media stream to the first video element
  let video = document.querySelector('video');
  if ("srcObject" in video) {
      video.srcObject = mediaStreamObj;
  } else {
      //old version
      video.src = window.URL.createObjectURL(mediaStreamObj);
  }
  
  video.onloadedmetadata = function(ev){
      video.play();
  };
  
  //add listeners for saving video/audio
  let start = document.getElementById("startTest");
  let stop = document.getElementById("finish");
  let mediaRecorder = new MediaRecorder(mediaStreamObj);
  let chunks = [];
  
  start.addEventListener('click', (ev)=>{
      mediaRecorder.start();
      console.log(mediaRecorder.state);
  })
  stop.addEventListener('click', (ev)=>{
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
  });
  mediaRecorder.ondataavailable = function(ev) {
      chunks.push(ev.data);
  }
  mediaRecorder.onstop = (ev)=>{
      let blob = new Blob(chunks, { 'type' : 'video/mp4;' });
      console.log(blob.size);
      chunks = [];
      let videoURL = window.URL.createObjectURL(blob);
  }
})
.catch(err=>{
  error = true;
})

window.onfocus = function(){
  if(isTestStarted){
    if(!active){
      chance--;
      if(chance === 0){
        document.getElementById("Test").style.display = "none";
        document.getElementById("resultBox").style.display = "block";
        drawTable();
      }else{
        document.getElementById("warningBlock").style.display = "block";
        document.getElementById("warning").innerHTML = "Don't move from your window. You will get only "+chance+" chances."
        active = true;
      }
    }
  }
};
window.onblur = function(){
  active = false;
};

setInterval(function() {
  if(isTestStarted){
    time--;
    document.getElementById("min").innerHTML = time;
    if(time == 0){
      document.getElementById("Test").style.display = "none";
      document.getElementById("resultBox").style.display = "block";
      drawTable();
    }
  }
}, 60 * 1000);