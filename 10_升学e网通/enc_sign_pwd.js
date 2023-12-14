const CryptoJS = require('crypto-js')
const md5 = require('crypto-js/md5')


//  密码加密部分
const key = CryptoJS
  .enc
  .Utf8
  .parse("20171109124536982017110912453698");

const iv = CryptoJS
  .enc
  .Utf8
  .parse('2017110912453698'); //十六位十六进制数作为密钥偏移量

const encrypt = (word) => {
    let srcs = CryptoJS
      .enc
      .Utf8
      .parse(word);
    let encrypted = CryptoJS
      .AES
      .encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
      });
    return encrypted
      .ciphertext
      .toString()
      .toUpperCase();
  }

// sign加密部分
const getNowTime = async () => {
    const localNowTime = new Date().getTime()
    return localNowTime
}
function sign() {
    const nowTime =  getNowTime()
    return md5(nowTime + 'bdc739ff2dcf').toString().toLocaleUpperCase()
}

function password(pwd) {
    let enc_pwd = encrypt(pwd)
    console.log(enc_pwd)
    return {
        enc_pwd
    }
}

function enc(pwd) {
    return {
        pwd: password(pwd),
        sign: sign()
    }
}

// console.log(enc(123456))
