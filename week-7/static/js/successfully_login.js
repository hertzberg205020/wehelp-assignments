async function getMemberInfo() {
    let ret = null;
    let content = document.getElementById('query_userName').value;
    let url = "/api/members?username=" + content;
    await fetch(url)
        .then(function (rsp) {
            return rsp.json();
        })
        .then(function (result) {
            ret = result
        });
    return ret;
}

function appendInfo(member_info_obj, wrapper, warm) {
    let container = document.getElementById(wrapper);
    let fragment = document.createDocumentFragment();
    let info = document.createElement("div");
    info.className = "append_data";
    if (member_info_obj != null) {
        info.appendChild(document.createTextNode("" + member_info_obj.data['name'] + ' (' + member_info_obj.data.username + ')'));
    } else {
        info.appendChild(document.createTextNode(warm));
    }

    fragment.appendChild(info);
    container.appendChild(fragment);

}

function showMemberInfo(member_info_obj, wrapper, warm) {
    let container = document.getElementById(wrapper);

    if (member_info_obj !== null && member_info_obj.data !== null) {
        // 有收到有效會員數據
        let info = "" + member_info_obj['data']['name'] + ' (' + member_info_obj['data'].username + ')';
        if (container.innerHTML !== "") {
            // 已經有查詢結果顯示，僅需更新資料
            document.querySelector('.append_data').textContent = info
            return;
        }
        // 添加查詢結果
        appendInfo(member_info_obj, wrapper, warm);
        return;
    }
    if (container.innerHTML !== "") {
        // 未收到有效會員數據，更新查詢下方顯示內容為警告訊息
        document.querySelector('.append_data').textContent = warm;
        return;
    }
    // 未收到有效會員數據，且無任何數據呈現，添加緊告內容
    appendInfo(null, wrapper, warm);
}

async function rename() {
    let ret = false;
    let newName = document.getElementById('new_name').value;
    let data = {
        'name': newName
    }
    let url = "/api/member";
    await fetch(url, {
        headers: {
            "Content-Type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(data), // 一定要傳字串格式
    })
        .then(function (rsp) {
            return rsp.json();
        })
        .then(function (result) {
            ret = result;
        });
    return ret;
}

function showRenameStat(res) {
    if (res !== null) {
        let container = document.getElementById('wrapper_rename_stat');

        if (typeof(res.ok) !== 'undefined') {
            container.innerText = '更新成功';
        }
        if (typeof(res.error) !== 'undefined') {
            container.innerText = '更新失敗';
        }

    }
}

async function main() {
    const queryMemberBtn = document.getElementById("query_member_btn");
    queryMemberBtn.addEventListener('click', async function () {
        let content = document.getElementById('query_userName').value;
        const container = document.getElementById('wrapper_member_info');
        if (content === '') {
            showMemberInfo(null, 'wrapper_member_info', "請輸入會員帳號");
            return;
        }
        let member_info_obj = await getMemberInfo();
        showMemberInfo(member_info_obj, 'wrapper_member_info', "查無此會員");
    });

    const renameBtn = document.getElementById("rename_btn");
    renameBtn.addEventListener('click', async function () {
        let content = document.getElementById('new_name');
        let res = await rename();
        showRenameStat(res);
    });
}

window.onload = main;