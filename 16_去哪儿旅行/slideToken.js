const cryptoJS = require('crypto-js')


// 轨迹
var openTime = Date.now()
var track = []
var preX = Math.round(Math.random()*30 + 430)
var preY = Math.round(Math.random()*10 + 500)
var preA = Math.round(Math.random()*440)

for ( let i = 0;  i < Math.round(Math.random()*3 + 2) ; i++) {
    var t = Date.now() % 1e5
    var f = "".concat(t, ";").concat(preX.toFixed(2), ";").concat(preY.toFixed(2), ";").concat(preA.toFixed(2));
    track.push(f)

    var newB = Math.round(Math.random()*60)
    while (preA + newB > 850) {
        newB = Math.round(Math.random()*60)
    }
    preX +=  
    preY = Math.round(Math.random()*10 + 500)
    var newA = Math.round(Math.random()*60)
    while (preA + newA > 440) {
        newA = Math.round(Math.random()*60)
    }
    preA +=  newA
}

track.push("".concat(Date.now() % 1e5, ";").concat(Math.round(Math.random()*30 + 850).toFixed(2), ";").concat(Math.round(Math.random()*10 + 500).toFixed(2), ";").concat(Math.round(Math.random()*10 + 440).toFixed(2)))

// 滑块轨迹信息
var sliderInfo = {
    "openTime": openTime ,
    "startTime": openTime + Math.round(Math.random()*1000 + 500),
    "endTime": openTime + Math.round(Math.random()*1000 + 1500),
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "uid": "0000f000306c5b987b60a047",  // 固定
    "track": track,
    "acc": [],
    "ori": [],
    "deviceMotion": [
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        },
        {
            "isTrusted": true
        }
    ]  // 不检测
}

var e = JSON.stringify(sliderInfo);
var result =  cryptoJS.AES.encrypt(cryptoJS.enc.Utf8.parse(e), cryptoJS.enc.Utf8.parse("227V2xYeHTARSh1R"), {
    mode: cryptoJS.mode.ECB,
    padding: cryptoJS.pad.Pkcs7
}).toString()



function slider(){
    return result
}