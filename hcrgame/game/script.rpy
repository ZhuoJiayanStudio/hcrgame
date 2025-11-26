define hcr = Character("火柴人")

label start:
    show 8
    """
    著作权由卓嘉彦（80\%）和张溯芃（20\%）共同拥有。\n
    官方网站https://hcrgame.wordpress.com/
    """
    hide 8
    menu:
        "火柴人游戏"
        "开始游戏":
            "游戏结束"
            return
        "结束游戏":
            "恭喜你，通过了第0关！"
            show background 1
            menu:
                "火柴人游戏 第1关"
                "向左走":
                    "恭喜你，通过了第1关"
                "向右走":
                    "恭喜你，通过了第1关"
                "两个门都是真的。"
            hide background 1

            show background 2
            menu:
                "火柴人游戏 第2关"
                "点击神秘按钮":
                    menu:
                        "向左走":
                            "恭喜你，通过了第2关"
                        "向右走":
                            "游戏结束"
                            return
                "向左走":
                    "游戏结束"
                    return
                "向右走":
                    "游戏结束"
                    return
            hide background 2

            show background 3
            menu:
                "火柴人游戏 第3关"
                "黄灯":
                    menu:
                        "走":
                            "游戏结束"
                            return
                        "不走":
                            "红灯"
                            menu:
                                "走":
                                    "游戏结束"
                                    return
                                "不走":
                                    "绿灯"
                                    menu:
                                        "走":
                                            "恭喜你，通过了第3关"
                                        "不走":
                                            "游戏结束"
                                            return
            hide background 3

            show background 4
            menu:
                "火柴人游戏 第3A关"
                "向左走":
                    "游戏结束"
                    return
                "向右走":
                    "游戏结束"
                    return
                "尝试飞天":
                    "恭喜你，通过了第3A关"
            hide background 4

            show background 5
            menu:
                "火柴人游戏 第5关"
                "向左走":
                    "游戏结束"
                    return
                "向右走":
                    "游戏结束"
                    return
                "尝试飞天":
                    menu:
                        "你飞了起来"
                        "向左飞":
                            "恭喜你，通过了第5关"
                        "向右飞":
                            "游戏结束"
                            return
            hide background 5

            show background 6
            menu:
                "火柴人游戏 第6关"
                "向左走":
                    "游戏结束"
                    return
                "向右走":
                    "游戏结束"
                    return
                "跳起来":
                    "恭喜你，通过了第6关"
            hide background 6

            show background 7
            menu:
                "火柴人游戏 第7关"
                "按下按钮":
                    "你变大了"
                    menu:
                        "按下按钮":
                            "你变小了"
                            menu:
                                "向右走":
                                    menu:
                                        "向左走":
                                            "游戏结束"
                                            return
                                        "向右走":
                                            "恭喜你，通过了第7关"
                        "向左走":
                            "游戏结束"
                            return
                        "向右走":
                            "游戏结束"
                            return
                "向左走":
                    "游戏结束"
                    return
                "向右走":
                    "游戏结束"
                    return
            hide background 7

            show background 8
            "火柴人游戏 第8关"
            hcr "好想去泉州玩"
            hcr "买张票吧"
            "火柴人要进行人机验证"
            menu:
                "请输入验证码的答案"
                "0.3":
                    "游戏结束"
                    return
                "0.30000000000004":
                    "验证通过"
                    "恭喜你，通过了第8关"
            hide background 8

            "没有照片，自己意会一下"
            "火柴人游戏 第9关"
            hcr "买张机票"
            menu:
                "北京大兴（PKX） —— 泉州晋江（JJN）"
                "5929":
                    "支付成功"
                    "恭喜你，通过了第9关"
                "8132":
                    "余额不足"
                    "游戏结束"
                    return
                "9189":
                    "余额不足"
                    "游戏结束"
                    return
                "8011":
                    "余额不足"
                    "游戏结束"
                    return
                "5931":
                    "余额不足"
                    "游戏结束"
                    return
                "5967":
                    "余额不足"
                    "游戏结束"
                    return