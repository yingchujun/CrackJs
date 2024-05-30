window = globalThis;;

(function(e) {
    function t(t) {
        for (var o, a, s = t[0], l = t[1], c = t[2], u = 0, p = []; u < s.length; u++)
            a = s[u],
            Object.prototype.hasOwnProperty.call(r, a) && r[a] && p.push(r[a][0]),
            r[a] = 0;
        for (o in l)
            Object.prototype.hasOwnProperty.call(l, o) && (e[o] = l[o]);
        d && d(t);
        while (p.length)
            p.shift()();
        return i.push.apply(i, c || []),
        n()
    }
    function n() {
        for (var e, t = 0; t < i.length; t++) {
            for (var n = i[t], o = !0, a = 1; a < n.length; a++) {
                var s = n[a];
                0 !== r[s] && (o = !1)
            }
            o && (i.splice(t--, 1),
            e = l(l.s = n[0]))
        }
        return e
    }
    var o = {}
      , a = {
        app: 0
    }
      , r = {
        app: 0
    }
      , i = [];
    function s(e) {
        return l.p + "js/" + ({
            "Group-Brand": "Group-Brand",
            "Group-Demo~Group-User": "Group-Demo~Group-User",
            "Group-Demo": "Group-Demo",
            "Group-Help": "Group-Help",
            "Group-Html~Group-Star~Group-User-Focus": "Group-Html~Group-Star~Group-User-Focus",
            "Group-Star": "Group-Star",
            "Group-User-Focus": "Group-User-Focus",
            "Group-Html": "Group-Html",
            "Group-Risk": "Group-Risk",
            "Group-Tools": "Group-Tools",
            "Group-User": "Group-User",
            "Group-Public": "Group-Public"
        }[e] || e) + ".1715247069177.js"
    }
    function l(t) {
        if (t == 'c8ba')
            return window;
        var n = o[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        console.log('name:',t)
        return e[t].call(n.exports, n, n.exports, l),
        n.l = !0,
        n.exports
    }
    l.e = function(e) {
        var t = []
          , n = {
            "Group-Brand": 1,
            "Group-Star": 1,
            "Group-User-Focus": 1,
            "Group-Html": 1,
            "Group-Risk": 1,
            "Group-Tools": 1,
            "Group-User": 1
        };
        a[e] ? t.push(a[e]) : 0 !== a[e] && n[e] && t.push(a[e] = new Promise((function(t, n) {
            for (var o = "css/" + ({
                "Group-Brand": "Group-Brand",
                "Group-Demo~Group-User": "Group-Demo~Group-User",
                "Group-Demo": "Group-Demo",
                "Group-Help": "Group-Help",
                "Group-Html~Group-Star~Group-User-Focus": "Group-Html~Group-Star~Group-User-Focus",
                "Group-Star": "Group-Star",
                "Group-User-Focus": "Group-User-Focus",
                "Group-Html": "Group-Html",
                "Group-Risk": "Group-Risk",
                "Group-Tools": "Group-Tools",
                "Group-User": "Group-User",
                "Group-Public": "Group-Public"
            }[e] || e) + "." + {
                "Group-Brand": "6e021003",
                "Group-Demo~Group-User": "31d6cfe0",
                "Group-Demo": "31d6cfe0",
                "Group-Help": "31d6cfe0",
                "Group-Html~Group-Star~Group-User-Focus": "31d6cfe0",
                "Group-Star": "f9edcdaf",
                "Group-User-Focus": "1336b200",
                "chunk-140484fa": "31d6cfe0",
                "Group-Html": "36e832d7",
                "Group-Risk": "34da6fc3",
                "Group-Tools": "84a16c17",
                "Group-User": "2eea4c78",
                "chunk-231e072a": "31d6cfe0",
                "chunk-4657e2c3": "31d6cfe0",
                "Group-Public": "31d6cfe0"
            }[e] + ".css", r = l.p + o, i = document.getElementsByTagName("link"), s = 0; s < i.length; s++) {
                var c = i[s]
                  , u = c.getAttribute("data-href") || c.getAttribute("href");
                if ("stylesheet" === c.rel && (u === o || u === r))
                    return t()
            }
            var p = document.getElementsByTagName("style");
            for (s = 0; s < p.length; s++) {
                c = p[s],
                u = c.getAttribute("data-href");
                if (u === o || u === r)
                    return t()
            }
            var d = document.createElement("link");
            d.rel = "stylesheet",
            d.type = "text/css",
            d.onload = t,
            d.onerror = function(t) {
                var o = t && t.target && t.target.src || r
                  , i = new Error("Loading CSS chunk " + e + " failed.\n(" + o + ")");
                i.code = "CSS_CHUNK_LOAD_FAILED",
                i.request = o,
                delete a[e],
                d.parentNode.removeChild(d),
                n(i)
            }
            ,
            d.href = r;
            var m = document.getElementsByTagName("head")[0];
            m.appendChild(d)
        }
        )).then((function() {
            a[e] = 0
        }
        )));
        var o = r[e];
        if (0 !== o)
            if (o)
                t.push(o[2]);
            else {
                var i = new Promise((function(t, n) {
                    o = r[e] = [t, n]
                }
                ));
                t.push(o[2] = i);
                var c, u = document.createElement("script");
                u.charset = "utf-8",
                u.timeout = 120,
                l.nc && u.setAttribute("nonce", l.nc),
                u.src = s(e);
                var p = new Error;
                c = function(t) {
                    u.onerror = u.onload = null,
                    clearTimeout(d);
                    var n = r[e];
                    if (0 !== n) {
                        if (n) {
                            var o = t && ("load" === t.type ? "missing" : t.type)
                              , a = t && t.target && t.target.src;
                            p.message = "Loading chunk " + e + " failed.\n(" + o + ": " + a + ")",
                            p.name = "ChunkLoadError",
                            p.type = o,
                            p.request = a,
                            n[1](p)
                        }
                        r[e] = void 0
                    }
                }
                ;
                var d = setTimeout((function() {
                    c({
                        type: "timeout",
                        target: u
                    })
                }
                ), 12e4);
                u.onerror = u.onload = c,
                document.head.appendChild(u)
            }
        return Promise.all(t)
    }
    ,
    l.m = e,
    l.c = o,
    l.d = function(e, t, n) {
        l.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: n
        })
    }
    ,
    l.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    l.t = function(e, t) {
        if (1 & t && (e = l(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var n = Object.create(null);
        if (l.r(n),
        Object.defineProperty(n, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var o in e)
                l.d(n, o, function(t) {
                    return e[t]
                }
                .bind(null, o));
        return n
    }
    ,
    l.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e["default"]
        }
        : function() {
            return e
        }
        ;
        return l.d(t, "a", t),
        t
    }
    ,
    l.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    l.p = "/",
    l.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    window.enc = l
    var c = window["webpackJsonp"] = window["webpackJsonp"] || []
      , u = c.push.bind(c);
    c.push = t,
    c = c.slice();
    for (var p = 0; p < c.length; p++)
        t(c[p]);
    var d = u;
    i.push([0, "chunk-vendors"]),
    n()
}
)({
    1: function(t, e) {},
    "21bf": function(t, e, r) {
        (function(e) {
            (function(e, r) {
                t.exports = r()
            }
            )(0, (function() {
                var t = t || function(t, n) {
                    var i;
                    if ("undefined" !== typeof window && window.crypto && (i = window.crypto),
                    "undefined" !== typeof self && self.crypto && (i = self.crypto),
                    "undefined" !== typeof globalThis && globalThis.crypto && (i = globalThis.crypto),
                    !i && "undefined" !== typeof window && window.msCrypto && (i = window.msCrypto),
                    !i && "undefined" !== typeof e && e.crypto && (i = e.crypto),
                    !i)
                        try {
                            i = r(1)
                        } catch (y) {}
                    var o = function() {
                        if (i) {
                            if ("function" === typeof i.getRandomValues)
                                try {
                                    return i.getRandomValues(new Uint32Array(1))[0]
                                } catch (y) {}
                            if ("function" === typeof i.randomBytes)
                                try {
                                    return i.randomBytes(4).readInt32LE()
                                } catch (y) {}
                        }
                        throw new Error("Native crypto module could not be used to get secure random number.")
                    }
                      , c = Object.create || function() {
                        function t() {}
                        return function(e) {
                            var r;
                            return t.prototype = e,
                            r = new t,
                            t.prototype = null,
                            r
                        }
                    }()
                      , s = {}
                      , a = s.lib = {}
                      , f = a.Base = function() {
                        return {
                            extend: function(t) {
                                var e = c(this);
                                return t && e.mixIn(t),
                                e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                                    e.$super.init.apply(this, arguments)
                                }
                                ),
                                e.init.prototype = e,
                                e.$super = this,
                                e
                            },
                            create: function() {
                                var t = this.extend();
                                return t.init.apply(t, arguments),
                                t
                            },
                            init: function() {},
                            mixIn: function(t) {
                                for (var e in t)
                                    t.hasOwnProperty(e) && (this[e] = t[e]);
                                t.hasOwnProperty("toString") && (this.toString = t.toString)
                            },
                            clone: function() {
                                return this.init.prototype.extend(this)
                            }
                        }
                    }()
                      , h = a.WordArray = f.extend({
                        init: function(t, e) {
                            t = this.words = t || [],
                            this.sigBytes = e != n ? e : 4 * t.length
                        },
                        toString: function(t) {
                            return (t || l).stringify(this)
                        },
                        concat: function(t) {
                            var e = this.words
                              , r = t.words
                              , n = this.sigBytes
                              , i = t.sigBytes;
                            if (this.clamp(),
                            n % 4)
                                for (var o = 0; o < i; o++) {
                                    var c = r[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                                    e[n + o >>> 2] |= c << 24 - (n + o) % 4 * 8
                                }
                            else
                                for (var s = 0; s < i; s += 4)
                                    e[n + s >>> 2] = r[s >>> 2];
                            return this.sigBytes += i,
                            this
                        },
                        clamp: function() {
                            var e = this.words
                              , r = this.sigBytes;
                            e[r >>> 2] &= 4294967295 << 32 - r % 4 * 8,
                            e.length = t.ceil(r / 4)
                        },
                        clone: function() {
                            var t = f.clone.call(this);
                            return t.words = this.words.slice(0),
                            t
                        },
                        random: function(t) {
                            for (var e = [], r = 0; r < t; r += 4)
                                e.push(o());
                            return new h.init(e,t)
                        }
                    })
                      , u = s.enc = {}
                      , l = u.Hex = {
                        stringify: function(t) {
                            for (var e = t.words, r = t.sigBytes, n = [], i = 0; i < r; i++) {
                                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                                n.push((o >>> 4).toString(16)),
                                n.push((15 & o).toString(16))
                            }
                            return n.join("")
                        },
                        parse: function(t) {
                            for (var e = t.length, r = [], n = 0; n < e; n += 2)
                                r[n >>> 3] |= parseInt(t.substr(n, 2), 16) << 24 - n % 8 * 4;
                            return new h.init(r,e / 2)
                        }
                    }
                      , d = u.Latin1 = {
                        stringify: function(t) {
                            for (var e = t.words, r = t.sigBytes, n = [], i = 0; i < r; i++) {
                                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                                n.push(String.fromCharCode(o))
                            }
                            return n.join("")
                        },
                        parse: function(t) {
                            for (var e = t.length, r = [], n = 0; n < e; n++)
                                r[n >>> 2] |= (255 & t.charCodeAt(n)) << 24 - n % 4 * 8;
                            return new h.init(r,e)
                        }
                    }
                      , p = u.Utf8 = {
                        stringify: function(t) {
                            try {
                                return decodeURIComponent(escape(d.stringify(t)))
                            } catch (e) {
                                throw new Error("Malformed UTF-8 data")
                            }
                        },
                        parse: function(t) {
                            return d.parse(unescape(encodeURIComponent(t)))
                        }
                    }
                      , _ = a.BufferedBlockAlgorithm = f.extend({
                        reset: function() {
                            this._data = new h.init,
                            this._nDataBytes = 0
                        },
                        _append: function(t) {
                            "string" == typeof t && (t = p.parse(t)),
                            this._data.concat(t),
                            this._nDataBytes += t.sigBytes
                        },
                        _process: function(e) {
                            var r, n = this._data, i = n.words, o = n.sigBytes, c = this.blockSize, s = 4 * c, a = o / s;
                            a = e ? t.ceil(a) : t.max((0 | a) - this._minBufferSize, 0);
                            var f = a * c
                              , u = t.min(4 * f, o);
                            if (f) {
                                for (var l = 0; l < f; l += c)
                                    this._doProcessBlock(i, l);
                                r = i.splice(0, f),
                                n.sigBytes -= u
                            }
                            return new h.init(r,u)
                        },
                        clone: function() {
                            var t = f.clone.call(this);
                            return t._data = this._data.clone(),
                            t
                        },
                        _minBufferSize: 0
                    })
                      , v = (a.Hasher = _.extend({
                        cfg: f.extend(),
                        init: function(t) {
                            this.cfg = this.cfg.extend(t),
                            this.reset()
                        },
                        reset: function() {
                            _.reset.call(this),
                            this._doReset()
                        },
                        update: function(t) {
                            return this._append(t),
                            this._process(),
                            this
                        },
                        finalize: function(t) {
                            t && this._append(t);
                            var e = this._doFinalize();
                            return e
                        },
                        blockSize: 16,
                        _createHelper: function(t) {
                            return function(e, r) {
                                return new t.init(r).finalize(e)
                            }
                        },
                        _createHmacHelper: function(t) {
                            return function(e, r) {
                                return new v.HMAC.init(t,r).finalize(e)
                            }
                        }
                    }),
                    s.algo = {});
                    return s
                }(Math);
                return t
            }
            ))
        }
        ).call(this, r("c8ba"))
    },
    1132: function(t, e, r) {
        (function(e, n) {
            t.exports = n(r("21bf"))
        }
        )(0, (function(t) {
            return function() {
                var e = t
                  , r = e.lib
                  , n = r.WordArray
                  , i = e.enc;
                i.Base64 = {
                    stringify: function(t) {
                        var e = t.words
                          , r = t.sigBytes
                          , n = this._map;
                        t.clamp();
                        for (var i = [], o = 0; o < r; o += 3)
                            for (var c = e[o >>> 2] >>> 24 - o % 4 * 8 & 255, s = e[o + 1 >>> 2] >>> 24 - (o + 1) % 4 * 8 & 255, a = e[o + 2 >>> 2] >>> 24 - (o + 2) % 4 * 8 & 255, f = c << 16 | s << 8 | a, h = 0; h < 4 && o + .75 * h < r; h++)
                                i.push(n.charAt(f >>> 6 * (3 - h) & 63));
                        var u = n.charAt(64);
                        if (u)
                            while (i.length % 4)
                                i.push(u);
                        return i.join("")
                    },
                    parse: function(t) {
                        var e = t.length
                          , r = this._map
                          , n = this._reverseMap;
                        if (!n) {
                            n = this._reverseMap = [];
                            for (var i = 0; i < r.length; i++)
                                n[r.charCodeAt(i)] = i
                        }
                        var c = r.charAt(64);
                        if (c) {
                            var s = t.indexOf(c);
                            -1 !== s && (e = s)
                        }
                        return o(t, e, n)
                    },
                    _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
                };
                function o(t, e, r) {
                    for (var i = [], o = 0, c = 0; c < e; c++)
                        if (c % 4) {
                            var s = r[t.charCodeAt(c - 1)] << c % 4 * 2
                              , a = r[t.charCodeAt(c)] >>> 6 - c % 4 * 2
                              , f = s | a;
                            i[o >>> 2] |= f << 24 - o % 4 * 8,
                            o++
                        }
                    return n.create(i, o)
                }
            }(),
            t
        }
        ))
    }
});





function encrypt(user, pwd) {
    var enc = window.enc(1132)
    var user = enc.enc.Base64.stringify(enc.enc.Utf8.parse(user))
    var pwd = enc.enc.Base64.stringify(enc.enc.Utf8.parse(pwd))
    return {user, pwd}
}