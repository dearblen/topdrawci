//系统相关配置
var CIRCUMSTANCE='production'; //取值为 simulate|production
var VERSION = '2.6.3';  //客户端版本
var GOD_MODE=0;
var BI_BASE_PATH2="http://111.10.31.197:82/2.gif";
var BI_BASE_PATH="http://111.11.189.11/1.gif";
var PLACEHOLDER_IMAGE_SRC="./image/placeholder_img.png";
var CONTENT_PROVIDER_ID = 16;  //搜狐片子
//读取cookies  Config 专用防止引起依赖问题
function getCookie4Config(strName){ 
    var arr,reg=new RegExp("(^| )"+strName+"=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg)){
	return decodeURIComponent(arr[2]); 
	}else{
	return null;
	}
} 
var g_strToken="2016f5a5ada24b86afebf6cd2ba30c70";



//业务相关配置

//首页视频区域播放列表
var INDEX_PLAY_LIST_SIZE=1;
var CONCERT_COVER_PLAY_LIST_SIZE=6;
var CONCERT_LIST_PLAY_LIST_SIZE=5;


var SELF_APPID="td8c5b326ca340265d";

/*鉴权常量*/

// var VALUE_ADDED_PRODUCT_ID=["20190910174230000000010"];
var VALUE_ADDED_PRODUCT_ID = ['20200116163200000000001','20190910174230000000010','20190910174230000000012','20190910174230000000013','20190910174230000000014'];//少儿频道包 包月 包季 半年包 包年 

var PRODUCT_PRICE=2000;//20元 
if(-1!=window.location.href.split('?')[0].indexOf('12:8080') || -1!=window.location.href.indexOf('file:///')){//本地和非现网环境下
    VALUE_ADDED_PRODUCT_ID="";//测试用的productId,价值1分钱 158020190626000001 158020190626000003 158020190611000050 158020190703000005
    PRODUCT_PRICE=1;//1分钱 
}

var PLACEHOLDER_IMAGE_SRC0="./image/placeholder_img.png";
var PLACEHOLDER_IMAGE_SRC = "./image/placeholder_img0.png";

var Global={
	'td8c5b326ca340265d':{//以appId作为子对象
        'appId':'td8c5b326ca340265d',
        'dirUrl':'childHall',
        'baseCId':''
    },
    'tda7e47f868313d9f5':{
        'appId':'tda7e47f868313d9f5',
        'dirUrl':'childCartoon',
        'baseCId':'236'
    },
    'tdd72ee5abf9a38754':{
        'appId':'tdd72ee5abf9a38754',
        'dirUrl':'childArt',
        'baseCId':'243'
    },
    'td7a74235419ac55ee':{
        'appId':'td7a74235419ac55ee',
        'dirUrl':'childClassical',
        'baseCId':'238'
    },
    'td8765403b3f38d1a8':{
        'appId':'td8765403b3f38d1a8',
        'dirUrl':'childEducation',
        'baseCId':'241'
    },
    'tdde7add064d218a84':{
        'appId':'tdde7add064d218a84',
        'dirUrl':'childEnglish',
        'baseCId':'239'
    },
    'td9eeab808e4d1a4b7':{
        'appId':'td9eeab808e4d1a4b7',
        'dirUrl':'childScience',
        'baseCId':'242'
    },
    'td9c60ab5ba1f3c44c':{
        'appId':'td9c60ab5ba1f3c44c',
        'dirUrl':'childSong',
        'baseCId':'237'
    },
    'td16283e54e262f207':{
        'appId':'td16283e54e262f207',
        'dirUrl':'childStory',
        'baseCId':'240'
    },
    'td3eef60f010559f43':{//安全
        "appId":"td3eef60f010559f43",
        "dirUrl":"childSafety",
        'baseCId':'245'
    },
    'tdaabcafa09311d2e9':{//玩具
        'appId':'tdaabcafa09311d2e9',
        'dirUrl':'childToy',
        'baseCId':'244'
    },
    'td793c7dca66cafb76':{//绘本
        'appId':'td793c7dca66cafb76',
        'dirUrl':'childPicture',
        'baseCId':'445'
    }
}

var g_oAppInfo = {
    "pages":{
        "index":"childHall/index.html",
        "category":"childHall/index.html",
        "history":"childHall/history.html",
        "search":"childHall/search.html",
        "collection":"childHall/collection.html",
        "program":"childHall/program.html",
        "movie":"childHall/movie.html",
        "achieveDetail":"childHall/achieveDetail.html",
        "myInfo":"childHall/myInfo.html",
        "mall":"childHall/mall.html",
        "indexEditor":"childHall/indexEditor.html",
        "hut":"childHall/hut1.html",
        "updateList":"childHall/updateList.html",
        "subscribe":"childHall/subscribe.html",
        "subscribeFrame":"childHall/subscribeFrame.html",
        "superstar":"childHall/superstar.html",
        "subjectList":"childHall/subjectList.html",
        "starDetail":"childHall/starDetail.html",
        "cartoonRanking":"childHall/cartoonRanking.html",
        "subjects":"childHall/subject/index.html",
        "subject":"childHall/subject_template/default/gate.html",
        "player" : "childHall/vPlayerFullScreen.html?t="+(new Date()).getTime(),
        "playerCartoon" : "childHall/vPlayerFullScreenCartoon.html?t="+(new Date()).getTime(),
        "academy":"childHall/academy/index.html",
    },
    "target" : {
        "detail01" : "/childHall/movie.html",
        "detail02" : "/childHall/program.html",
        "player01" : "/childHall/vPlayerFullScreen.html",
        "subject01": "/childHall/subject_template/default/gate.html",
    },
    "styles" : [
        "../css/common.css"
    ]
}