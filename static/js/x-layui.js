/*弹出层*/
/*
	参数解释：
	title	标题
	url		请求的url
	id		需要操作的数据id
	w		弹出层宽度（缺省调默认值）
	h		弹出层高度（缺省调默认值）
*/
function x_admin_show(title,url,w,h){
	if (title == null || title == '') {
		title=false;
	};
	if (url == null || url == '') {
		url="404.html";
	};
	if (w == null || w == '') {
		w=800;
	};
	if (h == null || h == '') {
		h=($(window).height() - 50);
	};

	layer.open({
		type: 2,
		area: [w+'px', h +'px'],
		fix: false, //不固定
		maxmin: true,
		shadeClose: true,
		shade:0.4,
		title: title,
		content: url
	});
}

/*关闭弹出框口*/
function x_admin_close(){
	var index = parent.layer.getFrameIndex(window.name);
	parent.layer.close(index);
}


/*
*
* 设置全局的 Ajax 异步 X-CSRFTOKEN
*
* */

layui.use(['element', 'layer', 'form'], function () {

	let $ = layui.jquery;//jquery

	// 获取 网页 cookie
	let cookies = document.cookie

	let _cookies = cookies.split(";")

	let ck_val = ""
	_cookies.forEach(cookie => {
		if (cookie.startsWith("csrftoken")) {
			ck_val = cookie.split("=")[1]
		}
	})

	$.ajaxSetup({

		headers: {
			"X-CSRFToken": ck_val
		}
	})

})