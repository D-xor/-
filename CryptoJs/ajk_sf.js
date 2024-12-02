const CryptoJS = require('crypto-js')

//_tanN
function _taN() {
    return {
        sdkv: "\u0033\u002e\u0030\u002e\u0031",
        busurl: "https://api.anjuke.com/web/general/captchaNew.html",
        useragent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        clienttype: '1'
    };
}

function AESEncrypt(taN, _2undefinedp) {
    // if (taN !== _taN()){
    //     taN = _taN()
    // }
    _2undefinedp = _2undefinedp['split']('')['reduce'](
        function(_PUi, _JrX, _JP9) {
            return _JP9 % 2 == 0 ? _PUi + '' : _PUi + _JrX;
        }, '');
    _2undefinedp = CryptoJS.enc.Utf8.parse(_2undefinedp)
    let encode_data = CryptoJS.AES.encrypt(JSON.stringify(taN), _2undefinedp, {
        iv: _2undefinedp,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    return encodeURIComponent(encode_data.toString());
}

console.log(AESEncrypt(_taN(), '2ce11cc9150f449b80926be814c9a6f8'))
console.log(AESEncrypt(_taN(), '2ce11cc9150f449b80926be814c9a6f8').length)

// var track = {
//     x: 107,
//     track: "47,5,0|47,6,45|54,6,52|60,6,61|68,6,69|76,6,76|83,6,83|89,6,91|95,5,99|107,4,108|108,4,116|111,4,123|115,2,132|116,2,139|119,2,147|119,1,155|120,0,163|120,-1,178|122,-2,187|123,-2,228|124,-2,235|125,-2,252|126,-2,261|127,-2,316|128,-2,324|131,-2,334|134,-3,341|139,-5,349|142,-6,355|143,-6,364|146,-6,371|147,-7,379|149,-7,387|151,-9,403|151,-9,419|151,-10,451|151,-10,468|152,-10,476|154,-11,492|154,-11,506|",
//     p: [0, 0]
// }


// var _session = "2ce11cc9150f449b80926be814c9a6f8"


// var data = AESEncrypt(track, _session)
// console.log(data.length)
// console.log(data)