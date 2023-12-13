window = globalThis;
window.enc = null
!function(e) {
    function n(data) {
        for (var n, t, d = data[0], l = data[1], f = data[2], i = 0, m = []; i < d.length; i++)
            t = d[i],
            Object.prototype.hasOwnProperty.call(o, t) && o[t] && m.push(o[t][0]),
            o[t] = 0;
        for (n in l)
            Object.prototype.hasOwnProperty.call(l, n) && (e[n] = l[n]);
        for (h && h(data); m.length; )
            m.shift()();
        return c.push.apply(c, f || []),
        r()
    }
    function r() {
        for (var e, i = 0; i < c.length; i++) {
            for (var n = c[i], r = !0, t = 1; t < n.length; t++) {
                var l = n[t];
                0 !== o[l] && (r = !1)
            }
            r && (c.splice(i--, 1),
            e = d(d.s = n[0]))
        }
        return e
    }
    var t = {}
      , o = {
        32: 0
    }
      , c = [];
    function d(n) {
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return e[n].call(r.exports, r, r.exports, d),
        r.l = !0,
        r.exports
    }
    d.e = function(e) {
        var n = []
          , r = o[e];
        if (0 !== r)
            if (r)
                n.push(r[2]);
            else {
                var t = new Promise((function(n, t) {
                    r = o[e] = [n, t]
                }
                ));
                n.push(r[2] = t);
                var c, script = document.createElement("script");
                script.charset = "utf-8",
                script.timeout = 120,
                d.nc && script.setAttribute("nonce", d.nc),
                script.src = function(e) {
                    return d.p + "" + ({
                        0: "commons/5b7f9e1d",
                        1: "vendors/f2d66b02",
                        2: "vendors/0f68e262",
                        5: "pages/album_detail/_index",
                        6: "pages/blackshark/index",
                        7: "pages/callback",
                        8: "pages/down/index",
                        9: "pages/downtingshu/index",
                        10: "pages/index",
                        11: "pages/logout/index",
                        12: "pages/musician/index",
                        13: "pages/musician/page",
                        14: "pages/mvplay/_index",
                        15: "pages/mvs/index",
                        16: "pages/play_detail/_index",
                        17: "pages/playlist_detail/_index",
                        18: "pages/playlists/index",
                        19: "pages/rankList/index",
                        20: "pages/search",
                        21: "pages/search/album",
                        22: "pages/search/list",
                        23: "pages/search/mv",
                        24: "pages/search/playlist",
                        25: "pages/search/singers",
                        26: "pages/singer_detail/_index",
                        27: "pages/singer_detail/index/album",
                        28: "pages/singer_detail/index/index",
                        29: "pages/singer_detail/index/info",
                        30: "pages/singer_detail/index/mv",
                        31: "pages/singers/index"
                    }[e] || e) + "." + {
                        0: "7f2c0cc",
                        1: "587cb3e",
                        2: "4deec49",
                        5: "ffee9c4",
                        6: "c52f389",
                        7: "ffdfc35",
                        8: "b4aa1c8",
                        9: "d621113",
                        10: "c3974e6",
                        11: "28722e8",
                        12: "d5af07f",
                        13: "5215e8f",
                        14: "f8ebf2a",
                        15: "1d8d1c3",
                        16: "2a37ece",
                        17: "64090ae",
                        18: "0407eb0",
                        19: "a5a4c3a",
                        20: "df68ca7",
                        21: "87fa638",
                        22: "7f3d05a",
                        23: "d5141ec",
                        24: "db31910",
                        25: "3b69ddc",
                        26: "5ca0d98",
                        27: "362866f",
                        28: "d44680b",
                        29: "c53e7d8",
                        30: "6c9f4d7",
                        31: "1cd60fe"
                    }[e] + ".js"
                }(e);
                var l = new Error;
                c = function(n) {
                    script.onerror = script.onload = null,
                    clearTimeout(f);
                    var r = o[e];
                    if (0 !== r) {
                        if (r) {
                            var t = n && ("load" === n.type ? "missing" : n.type)
                              , c = n && n.target && n.target.src;
                            l.message = "Loading chunk " + e + " failed.\n(" + t + ": " + c + ")",
                            l.name = "ChunkLoadError",
                            l.type = t,
                            l.request = c,
                            r[1](l)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var f = setTimeout((function() {
                    c({
                        type: "timeout",
                        target: script
                    })
                }
                ), 12e4);
                script.onerror = script.onload = c,
                document.head.appendChild(script)
            }
        return Promise.all(n)
    }
    ,
    d.m = e,
    d.c = t,
    d.d = function(e, n, r) {
        d.o(e, n) || Object.defineProperty(e, n, {
            enumerable: !0,
            get: r
        })
    }
    ,
    d.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    d.t = function(e, n) {
        if (1 & n && (e = d(e)),
        8 & n)
            return e;
        if (4 & n && "object" == typeof e && e && e.__esModule)
            return e;
        var r = Object.create(null);
        if (d.r(r),
        Object.defineProperty(r, "default", {
            enumerable: !0,
            value: e
        }),
        2 & n && "string" != typeof e)
            for (var t in e)
                d.d(r, t, function(n) {
                    return e[n]
                }
                .bind(null, t));
        return r
    }
    ,
    d.n = function(e) {
        var n = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return d.d(n, "a", n),
        n
    }
    ,
    d.o = function(object, e) {
        return Object.prototype.hasOwnProperty.call(object, e)
    }
    ,
    d.p = "https://h5static.kuwo.cn/www/kw-www/",
    d.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    window.enc = d;
    var l = window.webpackJsonp = window.webpackJsonp || []
      , f = l.push.bind(l);
    l.push = n,
    l = l.slice();
    for (var i = 0; i < l.length; i++)
        n(l[i]);
    var h = f;
    r()
}({
    1: function(t, e, n) {
        var r, o, l = n(204), c = n(205), d = 0, h = 0;
        t.exports = function(t, e, n) {
            var i = e && n || 0
              , b = e || []
              , f = (t = t || {}).node || r
              , v = void 0 !== t.clockseq ? t.clockseq : o;
            if (null == f || null == v) {
                var m = l();
                null == f && (f = r = [1 | m[0], m[1], m[2], m[3], m[4], m[5]]),
                null == v && (v = o = 16383 & (m[6] << 8 | m[7]))
            }
            var y = void 0 !== t.msecs ? t.msecs : (new Date).getTime()
              , w = void 0 !== t.nsecs ? t.nsecs : h + 1
              , dt = y - d + (w - h) / 1e4;
            if (dt < 0 && void 0 === t.clockseq && (v = v + 1 & 16383),
            (dt < 0 || y > d) && void 0 === t.nsecs && (w = 0),
            w >= 1e4)
                throw new Error("uuid.v1(): Can't create more than 10M uuids/sec");
            d = y,
            h = w,
            o = v;
            var x = (1e4 * (268435455 & (y += 122192928e5)) + w) % 4294967296;
            b[i++] = x >>> 24 & 255,
            b[i++] = x >>> 16 & 255,
            b[i++] = x >>> 8 & 255,
            b[i++] = 255 & x;
            var _ = y / 4294967296 * 1e4 & 268435455;
            b[i++] = _ >>> 8 & 255,
            b[i++] = 255 & _,
            b[i++] = _ >>> 24 & 15 | 16,
            b[i++] = _ >>> 16 & 255,
            b[i++] = v >>> 8 | 128,
            b[i++] = 255 & v;
            for (var A = 0; A < 6; ++A)
                b[i + A] = f[A];
            return e || c(b)
        }
    },
    204: function(t, e) {
        var n = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof window.msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto);
        if (n) {
            var r = new Uint8Array(16);
            t.exports = function() {
                return n(r),
                r
            }
        } else {
            var o = new Array(16);
            t.exports = function() {
                for (var t, i = 0; i < 16; i++)
                    0 == (3 & i) && (t = 4294967296 * Math.random()),
                    o[i] = t >>> ((3 & i) << 3) & 255;
                return o
            }
        }
    },
    205:function(t, e) {
        for (var n = [], i = 0; i < 256; ++i)
            n[i] = (i + 256).toString(16).substr(1);
        t.exports = function(t, e) {
            var i = e || 0
              , r = n;
            return [r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]]].join("")
        }
    }
});



function reqId() {
    const reqId = window.enc(1)()
    console.log(reqId)
    return reqId
}


reqId()