window = {
    navigator: {
      webdriver: false,
      appCodeName: "Mozilla",
      appName: "Netscape",
      appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
      userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    }
  };
document = {};
location = {}

setTimeout = function(func, time) {
    func()
}



function jsl_clearance_s(code) {
    eval(code)
    return document.cookie
}