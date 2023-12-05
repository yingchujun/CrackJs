var sinaSSOEncoder = sinaSSOEncoder || {};
    (function() {
        var a = 0
          , b = 8;
        this.hex_sha1 = function(a) {
            return i(c(h(a), a.length * b))
        }
        ;
        var c = function(a, b) {
            a[b >> 5] |= 128 << 24 - b % 32;
            a[(b + 64 >> 9 << 4) + 15] = b;
            var c = Array(80)
              , h = 1732584193
              , i = -271733879
              , j = -1732584194
              , k = 271733878
              , l = -1009589776;
            for (var m = 0; m < a.length; m += 16) {
                var n = h
                  , o = i
                  , p = j
                  , q = k
                  , r = l;
                for (var s = 0; s < 80; s++) {
                    s < 16 ? c[s] = a[m + s] : c[s] = g(c[s - 3] ^ c[s - 8] ^ c[s - 14] ^ c[s - 16], 1);
                    var t = f(f(g(h, 5), d(s, i, j, k)), f(f(l, c[s]), e(s)));
                    l = k;
                    k = j;
                    j = g(i, 30);
                    i = h;
                    h = t
                }
                h = f(h, n);
                i = f(i, o);
                j = f(j, p);
                k = f(k, q);
                l = f(l, r)
            }
            return [h, i, j, k, l]
        }
          , d = function(a, b, c, d) {
            return a < 20 ? b & c | ~b & d : a < 40 ? b ^ c ^ d : a < 60 ? b & c | b & d | c & d : b ^ c ^ d
        }
          , e = function(a) {
            return a < 20 ? 1518500249 : a < 40 ? 1859775393 : a < 60 ? -1894007588 : -899497514
        }
          , f = function(a, b) {
            var c = (a & 65535) + (b & 65535)
              , d = (a >> 16) + (b >> 16) + (c >> 16);
            return d << 16 | c & 65535
        }
          , g = function(a, b) {
            return a << b | a >>> 32 - b
        }
          , h = function(a) {
            var c = []
              , d = (1 << b) - 1;
            for (var e = 0; e < a.length * b; e += b)
                c[e >> 5] |= (a.charCodeAt(e / b) & d) << 24 - e % 32;
            return c
        }
          , i = function(b) {
            var c = a ? "0123456789ABCDEF" : "0123456789abcdef"
              , d = "";
            for (var e = 0; e < b.length * 4; e++)
                d += c.charAt(b[e >> 2] >> (3 - e % 4) * 8 + 4 & 15) + c.charAt(b[e >> 2] >> (3 - e % 4) * 8 & 15);
            return d
        }
          , j = function(a) {
            var b = ""
              , c = 0;
            for (; c < a.length; c++)
                b += "%" + k(a[c]);
            return decodeURIComponent(b)
        }
          , k = function(a) {
            var b = "0" + a.toString(16);
            return b.length <= 2 ? b : b.substr(1)
        };
        this.base64 = {
            encode: function(a) {
                a = "" + a;
                if (a == "")
                    return "";
                var b = "", c, d, e = "", f, g, h, i = "", j = 0;
                do {
                    c = a.charCodeAt(j++);
                    d = a.charCodeAt(j++);
                    e = a.charCodeAt(j++);
                    f = c >> 2;
                    g = (c & 3) << 4 | d >> 4;
                    h = (d & 15) << 2 | e >> 6;
                    i = e & 63;
                    isNaN(d) ? h = i = 64 : isNaN(e) && (i = 64);
                    b = b + this._keys.charAt(f) + this._keys.charAt(g) + this._keys.charAt(h) + this._keys.charAt(i);
                    c = d = e = "";
                    f = g = h = i = ""
                } while (j < a.length);
                return b
            },
            decode: function(a, b, c) {
                var d = function(a, b) {
                    for (var c = 0; c < a.length; c++)
                        if (a[c] === b)
                            return c;
                    return -1
                };
                typeof a == "string" && (a = a.split(""));
                var e = [], f, g, h = "", i, j, k, l = "";
                a.length % 4 == 0;
                var m = /[^A-Za-z0-9+\/=]/
                  , n = this._keys.split("");
                if (b == "urlsafe") {
                    m = /[^A-Za-z0-9-_=]/;
                    n = this._keys_urlsafe.split("")
                }
                if (b == "subp_v2") {
                    m = /[^A-Za-z0-9_=-]/;
                    n = this._subp_v2_keys.split("")
                }
                if (b == "subp_v3_3") {
                    m = /[^A-Za-z0-9-_.-]/;
                    n = this._subp_v3_keys_3.split("")
                }
                var o = 0;
                if (b == "binnary") {
                    n = [];
                    for (o = 0; o <= 64; o++)
                        n[o] = o + 128
                }
                if (b != "binnary" && m.test(a.join("")))
                    return c == "array" ? [] : "";
                o = 0;
                do {
                    i = d(n, a[o++]);
                    j = d(n, a[o++]);
                    k = d(n, a[o++]);
                    l = d(n, a[o++]);
                    f = i << 2 | j >> 4;
                    g = (j & 15) << 4 | k >> 2;
                    h = (k & 3) << 6 | l;
                    e.push(f);
                    k != 64 && k != -1 && e.push(g);
                    l != 64 && l != -1 && e.push(h);
                    f = g = h = "";
                    i = j = k = l = ""
                } while (o < a.length);
                if (c == "array")
                    return e;
                var p = ""
                  , q = 0;
                for (; q < e.lenth; q++)
                    p += String.fromCharCode(e[q]);
                return p
            },
            _keys: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
            _keys_urlsafe: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=",
            _subp_v2_keys: "uAL715W8e3jJCcNU0lT_FSXVgxpbEDdQ4vKaIOH2GBPtfzqsmYZo-wRM9i6hynrk=",
            _subp_v3_keys_3: "5WFh28sGziZTeS1lBxCK-HgPq9IdMUwknybo.LJrQD3uj_Va7pE0XfcNR4AOYvm6t"
        };
        this.Cookie = {
            decode: function(a) {
                var b = []
                  , c = a.substr(0, 3)
                  , d = a.substr(3);
                switch (c) {
                case "v01":
                    for (var e = 0; e < d.length; e += 2)
                        b.push(parseInt(d.substr(e, 2), 16));
                    return decodeURIComponent(j(sinaSSOEncoder.base64.decode(b, "binnary", "array")));
                case "v02":
                    d = d.replace(/\./g, "=");
                    b = sinaSSOEncoder.base64.decode(d, "urlsafe", "array");
                    return j(sinaSSOEncoder.base64.decode(b, "binnary", "array"));
                default:
                    return decodeURIComponent(a)
                }
            }
        };
        this.getSUBPCookie = {
            __parse: function(a) {
                var b, c, d, e, f, g = 0, h, i = {}, k = "", l = "";
                if (!a)
                    return i;
                do {
                    c = a[g];
                    b = ++g;
                    for (h = g; h < c + b; h++,
                    g++)
                        k += String.fromCharCode(a[h]);
                    e = a[g];
                    b = ++g;
                    if (k == "status" || k == "flag")
                        for (h = g; h < e + b; h++,
                        g++)
                            l += a[h];
                    else {
                        l = a.slice(b, e + b);
                        try {
                            l = j(l)
                        } catch (m) {
                            l = ""
                        }
                        g += e
                    }
                    i[k] = l;
                    k = "";
                    l = ""
                } while (g < a.length);
                return i
            },
            decode: function(a) {
                var b = [], c, d = a.substr(0, 3), e = decodeURIComponent(a.substr(3));
                switch (d) {
                case "002":
                    b = sinaSSOEncoder.base64.decode(e, "subp_v2", "array");
                    return sinaSSOEncoder.getSUBPCookie.__parse(b);
                case "003":
                    c = e.substr(0, 1);
                    e = e.substr(1);
                    b = sinaSSOEncoder.base64.decode(e, "subp_v3_" + c, "array");
                    return sinaSSOEncoder.getSUBPCookie.__parse(b);
                default:
                    return decodeURIComponent(a)
                }
            }
        }
    }
    ).call(sinaSSOEncoder);



    
let a = '15858585858'
let su = sinaSSOEncoder.base64.encode(a)
console.log(su)