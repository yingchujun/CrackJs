function encPwd(e, t, n) {
    var i = {}
      , r = {};
    !function(e) {
        function t(e) {
            var t = i
              , n = t.biDivideByRadixPower(e, this.k - 1)
              , r = t.biMultiply(n, this.mu)
              , o = t.biDivideByRadixPower(r, this.k + 1)
              , a = t.biModuloByRadixPower(e, this.k + 1)
              , s = t.biMultiply(o, this.modulus)
              , c = t.biModuloByRadixPower(s, this.k + 1)
              , l = t.biSubtract(a, c);
            l.isNeg && (l = t.biAdd(l, this.bkplus1));
            for (var u = 0 <= t.biCompare(l, this.modulus); u; )
                l = t.biSubtract(l, this.modulus),
                u = 0 <= t.biCompare(l, this.modulus);
            return l
        }
        function n(e, t) {
            var n = i.biMultiply(e, t);
            return this.modulo(n)
        }
        function r(e, t) {
            var n = new p;
            n.digits[0] = 1;
            for (var r = e, o = t; 0 != (1 & o.digits[0]) && (n = this.multiplyMod(n, r)),
            0 != (o = i.biShiftRight(o, 1)).digits[0] || 0 != i.biHighIndex(o); )
                r = this.multiplyMod(r, r);
            return n
        }
        function o(t, n, r) {
            var o = i;
            this.e = o.biFromHex(t),
            this.d = o.biFromHex(n),
            this.m = o.biFromHex(r),
            this.chunkSize = 2 * o.biHighIndex(this.m),
            this.radix = 16,
            this.barrett = new e.BarrettMu(this.m)
        }
        void 0 === e.RSAUtils && (e.RSAUtils = {});
        var a, s, c, l = 16, u = 65536, d = u - 1, p = e.BigInt = function(e) {
            this.digits = "boolean" == typeof e && 1 == e ? null : a.slice(0),
            this.isNeg = !1
        }
        ;
        i.setMaxDigits = function(e) {
            a = new Array(e);
            for (var t = 0; t < a.length; t++)
                a[t] = 0;
            s = new p,
            (c = new p).digits[0] = 1
        }
        ,
        i.setMaxDigits(20),
        i.biFromNumber = function(e) {
            var t = new p;
            t.isNeg = e < 0,
            e = Math.abs(e);
            for (var n = 0; 0 < e; )
                t.digits[n++] = e & d,
                e = Math.floor(e / u);
            return t
        }
        ;
        var f = i.biFromNumber(1e15);
        i.biFromDecimal = function(e) {
            for (var t, n = "-" == e.charAt(0), r = n ? 1 : 0; r < e.length && "0" == e.charAt(r); )
                ++r;
            if (r == e.length)
                t = new p;
            else {
                var o = (e.length - r) % 15;
                for (0 == o && (o = 15),
                t = i.biFromNumber(Number(e.substr(r, o))),
                r += o; r < e.length; )
                    t = i.biAdd(i.biMultiply(t, f), i.biFromNumber(Number(e.substr(r, 15)))),
                    r += 15;
                t.isNeg = n
            }
            return t
        }
        ,
        i.biCopy = function(e) {
            var t = new p(!0);
            return t.digits = e.digits.slice(0),
            t.isNeg = e.isNeg,
            t
        }
        ,
        i.reverseStr = function(e) {
            for (var t = "", n = e.length - 1; -1 < n; --n)
                t += e.charAt(n);
            return t
        }
        ;
        var h = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
        i.biToString = function(e, t) {
            var n = new p;
            n.digits[0] = t;
            for (var r = i.biDivideModulo(e, n), o = h[r[1].digits[0]]; 1 == i.biCompare(r[0], s); )
                r = i.biDivideModulo(r[0], n),
                digit = r[1].digits[0],
                o += h[r[1].digits[0]];
            return (e.isNeg ? "-" : "") + i.reverseStr(o)
        }
        ,
        i.biToDecimal = function(e) {
            var t = new p;
            t.digits[0] = 10;
            for (var n = i.biDivideModulo(e, t), r = String(n[1].digits[0]); 1 == i.biCompare(n[0], s); )
                n = i.biDivideModulo(n[0], t),
                r += String(n[1].digits[0]);
            return (e.isNeg ? "-" : "") + i.reverseStr(r)
        }
        ;
        var g = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
        i.digitToHex = function(e) {
            for (var t = "", n = 0; n < 4; ++n)
                t += g[15 & e],
                e >>>= 4;
            return i.reverseStr(t)
        }
        ,
        i.biToHex = function(e) {
            for (var t = "", n = (i.biHighIndex(e),
            i.biHighIndex(e)); -1 < n; --n)
                t += i.digitToHex(e.digits[n]);
            return t
        }
        ,
        i.charToHex = function(e) {
            return 48 <= e && e <= 57 ? e - 48 : 65 <= e && e <= 90 ? 10 + e - 65 : 97 <= e && e <= 122 ? 10 + e - 97 : 0
        }
        ,
        i.hexToDigit = function(e) {
            for (var t = 0, n = Math.min(e.length, 4), r = 0; r < n; ++r)
                t <<= 4,
                t |= i.charToHex(e.charCodeAt(r));
            return t
        }
        ,
        i.biFromHex = function(e) {
            for (var t = new p, n = e.length, r = 0; 0 < n; n -= 4,
            ++r)
                t.digits[r] = i.hexToDigit(e.substr(Math.max(n - 4, 0), Math.min(n, 4)));
            return t
        }
        ,
        i.biFromString = function(e, t) {
            var n = "-" == e.charAt(0)
              , r = n ? 1 : 0
              , o = new p
              , a = new p;
            a.digits[0] = 1;
            for (var s = e.length - 1; r <= s; s--) {
                var c = e.charCodeAt(s)
                  , l = i.charToHex(c)
                  , u = i.biMultiplyDigit(a, l);
                o = i.biAdd(o, u),
                a = i.biMultiplyDigit(a, t)
            }
            return o.isNeg = n,
            o
        }
        ,
        i.biDump = function(e) {
            return (e.isNeg ? "-" : "") + e.digits.join(" ")
        }
        ,
        i.biAdd = function(e, t) {
            var n;
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                n = i.biSubtract(e, t),
                t.isNeg = !t.isNeg;
            else {
                n = new p;
                for (var r, o = 0, a = 0; a < e.digits.length; ++a)
                    r = e.digits[a] + t.digits[a] + o,
                    n.digits[a] = r % u,
                    o = Number(u <= r);
                n.isNeg = e.isNeg
            }
            return n
        }
        ,
        i.biSubtract = function(e, t) {
            var n;
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                n = i.biAdd(e, t),
                t.isNeg = !t.isNeg;
            else {
                var r, o;
                n = new p;
                for (var a = o = 0; a < e.digits.length; ++a)
                    r = e.digits[a] - t.digits[a] + o,
                    n.digits[a] = r % u,
                    n.digits[a] < 0 && (n.digits[a] += u),
                    o = 0 - Number(r < 0);
                if (-1 == o) {
                    for (a = o = 0; a < e.digits.length; ++a)
                        r = 0 - n.digits[a] + o,
                        n.digits[a] = r % u,
                        n.digits[a] < 0 && (n.digits[a] += u),
                        o = 0 - Number(r < 0);
                    n.isNeg = !e.isNeg
                } else
                    n.isNeg = e.isNeg
            }
            return n
        }
        ,
        i.biHighIndex = function(e) {
            for (var t = e.digits.length - 1; 0 < t && 0 == e.digits[t]; )
                --t;
            return t
        }
        ,
        i.biNumBits = function(e) {
            var t, n = i.biHighIndex(e), r = e.digits[n], o = (n + 1) * l;
            for (t = o; o - l < t && 0 == (32768 & r); --t)
                r <<= 1;
            return t
        }
        ,
        i.biMultiply = function(e, t) {
            for (var n, r, o, a, s = new p, c = i.biHighIndex(e), l = i.biHighIndex(t), u = 0; u <= l; ++u) {
                for (o = u,
                a = n = 0; a <= c; ++a,
                ++o)
                    r = s.digits[o] + e.digits[a] * t.digits[u] + n,
                    s.digits[o] = r & d,
                    n = r >>> 16;
                s.digits[u + c + 1] = n
            }
            return s.isNeg = e.isNeg != t.isNeg,
            s
        }
        ,
        i.biMultiplyDigit = function(e, t) {
            var n, r, o, a;
            a = new p,
            n = i.biHighIndex(e);
            for (var s = r = 0; s <= n; ++s)
                o = a.digits[s] + e.digits[s] * t + r,
                a.digits[s] = o & d,
                r = o >>> 16;
            return a.digits[1 + n] = r,
            a
        }
        ,
        i.arrayCopy = function(e, t, n, i, r) {
            for (var o = Math.min(t + r, e.length), a = t, s = i; a < o; ++a,
            ++s)
                n[s] = e[a]
        }
        ;
        var m = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
        i.biShiftLeft = function(e, t) {
            var n = Math.floor(t / l)
              , r = new p;
            i.arrayCopy(e.digits, 0, r.digits, n, r.digits.length - n);
            for (var o = t % l, a = l - o, s = r.digits.length - 1, c = s - 1; 0 < s; --s,
            --c)
                r.digits[s] = r.digits[s] << o & d | (r.digits[c] & m[o]) >>> a;
            return r.digits[0] = r.digits[s] << o & d,
            r.isNeg = e.isNeg,
            r
        }
        ;
        var y = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
        i.biShiftRight = function(e, t) {
            var n = Math.floor(t / l)
              , r = new p;
            i.arrayCopy(e.digits, n, r.digits, 0, e.digits.length - n);
            for (var o = t % l, a = l - o, s = 0, c = s + 1; s < r.digits.length - 1; ++s,
            ++c)
                r.digits[s] = r.digits[s] >>> o | (r.digits[c] & y[o]) << a;
            return r.digits[r.digits.length - 1] >>>= o,
            r.isNeg = e.isNeg,
            r
        }
        ,
        i.biMultiplyByRadixPower = function(e, t) {
            var n = new p;
            return i.arrayCopy(e.digits, 0, n.digits, t, n.digits.length - t),
            n
        }
        ,
        i.biDivideByRadixPower = function(e, t) {
            var n = new p;
            return i.arrayCopy(e.digits, t, n.digits, 0, n.digits.length - t),
            n
        }
        ,
        i.biModuloByRadixPower = function(e, t) {
            var n = new p;
            return i.arrayCopy(e.digits, 0, n.digits, 0, t),
            n
        }
        ,
        i.biCompare = function(e, t) {
            if (e.isNeg != t.isNeg)
                return 1 - 2 * Number(e.isNeg);
            for (var n = e.digits.length - 1; 0 <= n; --n)
                if (e.digits[n] != t.digits[n])
                    return e.isNeg ? 1 - 2 * Number(e.digits[n] > t.digits[n]) : 1 - 2 * Number(e.digits[n] < t.digits[n]);
            return 0
        }
        ,
        i.biDivideModulo = function(e, t) {
            var n, r, o = i.biNumBits(e), a = i.biNumBits(t), s = t.isNeg;
            if (o < a)
                return e.isNeg ? ((n = i.biCopy(c)).isNeg = !t.isNeg,
                e.isNeg = !1,
                t.isNeg = !1,
                r = biSubtract(t, e),
                e.isNeg = !0,
                t.isNeg = s) : (n = new p,
                r = i.biCopy(e)),
                [n, r];
            n = new p,
            r = e;
            for (var f = Math.ceil(a / l) - 1, h = 0; t.digits[f] < 32768; )
                t = i.biShiftLeft(t, 1),
                ++h,
                ++a,
                f = Math.ceil(a / l) - 1;
            r = i.biShiftLeft(r, h),
            o += h;
            for (var g = Math.ceil(o / l) - 1, m = i.biMultiplyByRadixPower(t, g - f); -1 != i.biCompare(r, m); )
                ++n.digits[g - f],
                r = i.biSubtract(r, m);
            for (var y = g; f < y; --y) {
                var v = y >= r.digits.length ? 0 : r.digits[y]
                  , b = y - 1 >= r.digits.length ? 0 : r.digits[y - 1]
                  , x = y - 2 >= r.digits.length ? 0 : r.digits[y - 2]
                  , k = f >= t.digits.length ? 0 : t.digits[f]
                  , w = f - 1 >= t.digits.length ? 0 : t.digits[f - 1];
                n.digits[y - f - 1] = v == k ? d : Math.floor((v * u + b) / k);
                for (var C = n.digits[y - f - 1] * (k * u + w), T = 4294967296 * v + (b * u + x); T < C; )
                    --n.digits[y - f - 1],
                    C = n.digits[y - f - 1] * (k * u | w),
                    T = v * u * u + (b * u + x);
                m = i.biMultiplyByRadixPower(t, y - f - 1),
                (r = i.biSubtract(r, i.biMultiplyDigit(m, n.digits[y - f - 1]))).isNeg && (r = i.biAdd(r, m),
                --n.digits[y - f - 1])
            }
            return r = i.biShiftRight(r, h),
            n.isNeg = e.isNeg != s,
            e.isNeg && (n = s ? i.biAdd(n, c) : i.biSubtract(n, c),
            t = i.biShiftRight(t, h),
            r = i.biSubtract(t, r)),
            0 == r.digits[0] && 0 == i.biHighIndex(r) && (r.isNeg = !1),
            [n, r]
        }
        ,
        i.biDivide = function(e, t) {
            return i.biDivideModulo(e, t)[0]
        }
        ,
        i.biModulo = function(e, t) {
            return i.biDivideModulo(e, t)[1]
        }
        ,
        i.biMultiplyMod = function(e, t, n) {
            return i.biModulo(i.biMultiply(e, t), n)
        }
        ,
        i.biPow = function(e, t) {
            for (var n = c, r = e; 0 != (1 & t) && (n = i.biMultiply(n, r)),
            0 != (t >>= 1); )
                r = i.biMultiply(r, r);
            return n
        }
        ,
        i.biPowMod = function(e, t, n) {
            for (var r = c, o = e, a = t; 0 != (1 & a.digits[0]) && (r = i.biMultiplyMod(r, o, n)),
            0 != (a = i.biShiftRight(a, 1)).digits[0] || 0 != i.biHighIndex(a); )
                o = i.biMultiplyMod(o, o, n);
            return r
        }
        ,
        e.BarrettMu = function(e) {
            this.modulus = i.biCopy(e),
            this.k = i.biHighIndex(this.modulus) + 1;
            var o = new p;
            o.digits[2 * this.k] = 1,
            this.mu = i.biDivide(o, this.modulus),
            this.bkplus1 = new p,
            this.bkplus1.digits[this.k + 1] = 1,
            this.modulo = t,
            this.multiplyMod = n,
            this.powMod = r
        }
        ,
        i.getKeyPair = function(e, t, n) {
            return new o(e,t,n)
        }
        ,
        void 0 === e.twoDigit && (e.twoDigit = function(e) {
            return (e < 10 ? "0" : "") + String(e)
        }
        ),
        i.encryptedString = function(e, t) {
            for (var n = [], r = t.length, o = 0; o < r; )
                n[o] = t.charCodeAt(o),
                o++;
            for (; n.length % e.chunkSize != 0; )
                n[o++] = 0;
            var a, s, c, l = n.length, u = "";
            for (o = 0; o < l; o += e.chunkSize) {
                for (c = new p,
                a = 0,
                s = o; s < o + e.chunkSize; ++a)
                    c.digits[a] = n[s++],
                    c.digits[a] += n[s++] << 8;
                var d = e.barrett.powMod(c, e.e);
                u += (16 == e.radix ? i.biToHex(d) : i.biToString(d, e.radix)) + " "
            }
            return u.substring(0, u.length - 1)
        }
        ,
        i.decryptedString = function(e, t) {
            var n, r, o, a = t.split(" "), s = "";
            for (n = 0; n < a.length; ++n) {
                var c;
                for (c = 16 == e.radix ? i.biFromHex(a[n]) : i.biFromString(a[n], e.radix),
                o = e.barrett.powMod(c, e.d),
                r = 0; r <= i.biHighIndex(o); ++r)
                    s += String.fromCharCode(255 & o.digits[r], o.digits[r] >> 8)
            }
            return 0 == s.charCodeAt(s.length - 1) && (s = s.substring(0, s.length - 1)),
            s
        }
        ,
        i.setMaxDigits(130)
    }(r);
    var o = i.getKeyPair(t, "", n);
    return i.encryptedString(o, e)
}



function enc(pwd) {
    var rsaExponent = "010001"
    var rsaModulus = "008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f"
    var r = 1411093327735 - (new Date).getTime()
    var o = (new Date).getTime() + r;
    return encPwd(o + encodeURIComponent(pwd), rsaExponent, rsaModulus)
}

console.log(enc('125874'))

