var minha = document.getElementsByClassName('video-feed-item-wrapper');
minha[1].getAttribute("href")
content= []
max=minha.length;
for(var i = 0 ; i < max; i++ ){
 content.push(minha[i].getAttribute("href"));
//  console.log(minha[i].getAttribute("href"))
//  	minha[i].getAttribute("href")
}
console.log(content[7]);;
// console.log(max)

var saveData = (function () {
var a = document.createElement("a");
// document.body.appendChild(a);
// a.style = "display: none";
return function (data, fileName) {
    var json = JSON.stringify(data),
        blob = new Blob([json], {type: "octet/stream"}),
        url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);
};
}());

var data = {content, d: new Date() },
    fileName = "my-download.json";

saveData(data, fileName);

