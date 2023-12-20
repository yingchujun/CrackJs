const CryptoJs = require('crypto-js')


function dec_data(t) {
    var m = CryptoJs.enc.Utf8.parse("0123456789ABCDEF");
    var f = CryptoJs.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
    var e = CryptoJs.enc.Hex.parse(t)
    var n = CryptoJs.enc.Base64.stringify(e)
    var a = CryptoJs.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    })
    var r = a.toString(CryptoJs.enc.Utf8);
    
    return r.toString()
}
