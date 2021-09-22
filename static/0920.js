$(document).ready(function () {
        });

        function stockselection() {
            $.ajax({
                type: "POST",
                url: '/stock',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({"market": "market-1", "sector": "sector-1", "tag": "tag-1"}),
                success: function (response) {

                }
            })
        }

        function stockinfos1() {
                $.ajax({
                    type: "GET",
                    url: "/stock",
                    data: {},
                    success: function (response) {
                        let info = response['info']
                        lists1(info[0])
                    }
                })
            }

            function lists1(info) {
                $.ajax({
                    type: "GET",
                    url: `/markets?info_give=${info}`,
                    data: {},
                    success: function (response) {
                        let market = response
                        $('#start').empty()
                        let temp_html = ``
                        temp_html = `<div class="input">`
                        $('#start').append(temp_html)
                        temp_html = ``
                        for(let i = 0; i < market.length; i++){
                            temp_html = `<div>
                                            <input type="radio" name="chk_info" value="${market[i]['code']}">${market[i]['name']}
                                        </div>`
                            $('#start').append(temp_html)
                        }
                        temp_html = `<button type="button" class="btn btn-success" onclick="lists2()">다음</button>
                                    </div>`
                        $('#start').append(temp_html)

                    }
                })
            }
