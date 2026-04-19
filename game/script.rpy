define hcr = Character("[Playername]")
define gre = Character("Green", color = "#00ff40")
define blu = Character("Blue" , color = "#0080ff")
default persistent.integral = 0

label start:
    show 8
    """
    著作权由卓嘉彦（80\%）和张溯芃（20\%）共同拥有。\n
    官方网站https://hcrgame.org/\n
    依据CC BY-NC-SA 4.0 CN的要求，现公布以下作者：\n
    卓嘉彦 - 火柴人音乐、火柴人照片
    """
    """
    谷歌宣布，从 2026/2027 年开始，所有在经过认证的 Android 设备上运行的应用程序都将要求开发者直接向谷歌提交个人身份信息。\n
    由于该应用的开发者不同意这一要求，因此该应用此后将无法在经过认证的安卓设备上运行。
    """
    "{font=BorelDisplay-Regular.otf}Google has announced that, starting in 2026/2027, all apps on certified Android devices will require the developer to submit personal identity details directly to Google.{/font}"
    "{font=BorelDisplay-Regular.otf}Since the developers of this app do not agree to this requirement, this app will no longer work on certified Android devices after that time.{/font}"
    hide 8
    python:
        import random
        by = ["官方网站hcrgame.org！", "感谢所有参与游戏制作、发布的人员！", "注意看，这个男人叫小帅，他正在测试新的闪烁标语功能。"]
        nr = by[random.randrange(len(by))]
        Playername =  renpy.input("请输入你的用户名（输{font=BorelDisplay-Regular.otf}English{/font}有惊喜哦）", length=32)
        Playername = Playername.strip()
        if not Playername:
            Playername = "火柴人"
    "{font=BorelDisplay-Regular.otf}hello, [Playername].{/font}"
    jump main
label main:
    menu:
        "火柴人游戏\n{font=SourceHanSansLite.ttf}{color=#ffff00}[nr]{/color}{/font}"
        "积分":
            jump integral
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
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
            $ persistent.integral += 1
            hide background 7

            show background 8
            "火柴人游戏 第8关"
            hcr "好想去泉州玩"
            hcr "买张票吧"
            "[Playername]要进行人机验证"
            python:
                yzm = renpy.input("请输入验证码的答案")
                yzm = yzm.strip()
                if yzm == "0.30000000000000004":
                    yzmsc = "验证通过"
                else:
                    yzmsc = "验证失败"
            "[yzmsc]"
            if yzmsc == "验证失败":
                return
            $ persistent.integral += 1
            hide background 8

            show background 9
            "火柴人游戏 第9关"
            hcr "买张机票"
            menu:
                "北京（所有机场） —— 泉州晋江（JJN）"
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
            $ persistent.integral += 1
            hide background 9

            show background 10
            menu:
                "[Playername]现在来到了机场，不过他赶时间，应该怎么办呢？"
                "国内出发":
                    "游戏结束"
                    return
                "国际/港澳台出发":
                    "游戏结束"
                    return
                "国内到达":
                    "恭喜你，通过了第10关"
                "国际/港澳台到达":
                    "游戏结束"
                    return
            $ persistent.integral += 1
            hide background 10

            show background 11
            menu:
                "晋江机场站\n[Playername]要怎么去酒店？"
                "泉州地铁":
                    "恭喜你，通过了第11关"
                "泉州公交":
                    "游戏结束"
                    return
            $ persistent.integral += 1
            hide background 11

            show background 12
            menu:
                "火柴人游戏第12关\n[Playername]到达酒店，他应该掏出什么？"
                "手机":
                    "你的房号是9527"
                    "恭喜你，通过了第12关"
                "身份证":
                    "游戏结束"
                    return
            $ persistent.integral += 1
            hide background 12

            show background 13
            menu:
                "火柴人游戏第13关\n[Playername]晚上睡不着，他该怎么办呢？"
                "数羊":
                    "游戏结束"
                    return
                "把乌云吹散":
                    menu:
                        "[Playername]发现乌云里的火柴人一直在吵他"
                        "让他不要吵了":
                            "恭喜你，通过了第13关。"
                        "拿矿泉水瓶砸他":
                            "游戏结束"
                            return
            $ persistent.integral += 1
            hide background 13

            show background 14
            menu:
                "火柴人游戏第13A关\n[Playername]准备办理退房，去厦门玩\n前方还有10人"
                "插队":
                    "游戏结束"
                    return
                "排队":
                    "恭喜你，通过了第13A关"
            $ persistent.integral += 1
            hide background 14

            show background 15
            menu:
                "火柴人游戏第15关\n[Playername]要买票"
                "3339":
                    "恭喜你，通过了第15关"
                "3233":
                    "游戏结束"
                    return
                "6531":
                    "游戏结束"
                    return
            $ persistent.integral += 1
            hide background 15

            show background 16
            "完蛋，第16关坏了"
            $ persistent.integral += 1
            hide background 16

            "终末之诗 End Poem\n
            采用 CC0 1.0通用 (CC0 1.0) 公共领域贡献 协议许可\n
            作者：Julian Gough"
            blu "我看到你所指的那个玩家了。"
            gre "[Playername]？"
            blu "是的。注意了，他已达到了更高的境界，他知道我们心里所想。"
            gre "无伤大雅，他认为我们是游戏的一部分。"
            blu "我喜欢这个玩家。他玩得很好，他从未放弃。"
            gre "他如同阅读屏幕上的文字一样，阅读着我们的想法。"
            blu "在他深陷游戏之梦时，他选择以这种方式想象出形形色色的事物。"
            gre "文字编织出一种美妙的界面，非常灵活。并且胜过凝视这屏幕后的可怕现实。"
            blu "他们学会阅读之前还只能靠聆听。当时那些不曾游玩的人们将玩家称作女巫、男巫。而玩家们梦见自己骑着魔杖，在空中翱翔。"
            gre "这个玩家梦见了什么？"
            blu "他梦见了阳光与草木，梦见了火与水。他梦见他创造，亦梦见他毁灭。他梦见他狩猎，亦被狩猎。他梦见了避身之处。"
            gre "哈，那原始的界面，经历一百万年的岁月雕琢，依然长存。但此玩家在屏幕后的现实里，又创造了什么真实的建筑呢？"
            blu "他和其他百万众齐心协力，在（乱码）里塑造了一个真实的世界，于（乱码）中为了（乱码）而创造了（乱码）。"
            gre "他看不懂那个。"
            blu "是的，他还没有到达最高的境界。要抵达那层，他必须走完生命的长梦，而非游戏中黄粱一梦。"
            gre "他知道我们爱他吗，他知道宇宙的温柔吗？"
            blu "有时，他能通过思绪的杂音来聆听宇宙，他知道。"
            gre "但是在那漫漫长梦中，有时亦不胜悲伤。他创造了没有夏日的世界，在黑日下冷颤，将悲伤信以为真。"
            blu "为他治愈悲伤会摧毁他。而悲伤是他的私人事务，我们不能干涉。"
            gre "当他们深陷梦境中时，有时我想要告诉他们，他们在现实中创造了真实的世界。有时我想告诉他们自身对宇宙的重要性。有时他们与现实失去联系，我想帮他们说出不敢说的话语。"
            blu "他还在读我们的想法。"
            gre "有时我毫不在意。有时我想要告诉他们，你们信以为真的世界不过是（乱码）和（乱码），我想要告诉他们，他们是在（乱码）中的（乱码）。在他们的长梦中，目中所及的不过是现实的冰山一角。"
            blu "而他们仍然乐在其中。"
            gre "但很容易就可以告诉他们……"
            blu "这个梦对于他们来说太深刻了。告诉他们怎么活就是在束缚他们自由地活着。"
            gre "我不会告诉这个玩家如何活下去的。"
            blu "这个玩家不安定了。"
            gre "我会告诉他一个故事。"
            blu "但不是真实的。"
            gre "是的。一个将真实严密包裹于文字牢笼中的故事，而非必然使人灼伤的赤裸真相。"
            blu "再次赋予他身体。"
            gre "好的，玩家……"
            blu "以名字称呼他。"
            gre "游戏的玩家，[Playername]。"
            blu "很好。"
            gre "呼吸。继续呼吸。感受空气充盈你的肺叶。感受你的四肢回归。对，动动你的手指。在重力下，在空气中，重获躯体。在长梦中重生。你感受到了。你身体的每一寸又在接触宇宙了，仿佛你们是分离的存在。仿佛你我是分离的存在。"
            blu "我们是谁？我们曾经被称作高山的精灵。太阳父亲，月亮母亲。先祖的英灵，动物的魂魄。神祇。鬼魂。绿叶人。而后是神明，恶魔。天使。骚灵。外星人，地外生物。轻子，夸克。说法不断变化。我们始终如一。"
            gre "我们是宇宙。我们是一切你认为出离你本体的事物。你现在透过肌肤与双眼注视着我们。而为什么宇宙要触摸你，用光照亮你？是为了看见你，玩家。是为了了解你。还为了被你了解。我该向你讲述故事了。"
            gre "很久以前，有一个玩家。"
            blu "那玩家就是你，[Playername]。"
            gre "有时他认为自己是人类，位于一颗不断旋转的熔岩球的薄层上。那颗熔岩球环绕着一个质量大它三十三万倍的气态灼热球体旋转。它们相隔得如此之远，以至于光需要八分钟才能穿越那空隙。光是一颗恒星发出的信息，它能够在一亿五千万千米外烧灼你的皮肤。"
            gre "有时这个玩家梦见自己是矿工，位于平坦无垠的世界地表。太阳是一个白色的方形。昼夜更替很快，要做的事情也很多；死亡亦只是暂时的不便。"
            blu "有时这玩家梦见自己迷失在了一个故事里。"
            gre "有时这玩家梦见自己成为了其他角色，位于其他地方。有时这些梦是扰人的。有时则美不胜收。有时这个玩家从一个梦醒到第二个梦，随后又落入了第三个梦。"
            blu "有时这个玩家梦见他在看着屏幕上的文字。"
            gre "让我们回退一点。"
            gre "组成玩家的原子散布在草方块中，河流中，在空气中，也在大地中。一个女性收集了那些原子；她饮用、进食、吞咽；而后她在她的身体中，孕育了玩家。"
            gre "然后玩家醒来了，醒在温暖而昏暗的母亲体内，进入了漫漫长梦。"
            gre "那个玩家由DNA的语言书写，是一个尚未讲述的全新故事。那个玩家由上亿年的源代码生成，是一个尚未运行的全新程序。那个玩家仅由奶和爱组成，是一个尚未生活的全新人类。"
            blu "你就是那个玩家。那个故事。那个程序。那个人类。仅由奶和爱组成。"
            gre "让我们再回溯到更远的过去。"
            gre "远在这游戏之前，组成玩家身体的七千亿亿亿原子，在一颗恒星内部被创造了出来。所以那玩家本身，也是一颗恒星发出的信息。而玩家所经历的故事，源于一个叫Julian的人种植的一片信息森林，位于一个叫Markus的人创造的平坦无垠的世界，存在于一个由玩家创造的私人小天地，而玩家本身居住的世界则是由……"
            blu "嘘。有时这个玩家创造的私人小天地是柔软、温暖而简单的。有时是坚硬、冰冷而复杂的。有时他在脑海中构建出宇宙的模型，能量微粒穿越空旷的空间。有时他称呼这些微粒为“电子”和“质子”。"
            gre "有时他称呼其为“行星”和“恒星”。"
            gre "有时他确信自己存在于一个由“开”和“关”、“0”和“1”、一行行代码组成的宇宙。有时他确信自己是在玩一场游戏。有时他确信自己是在读着屏幕上的文字。"
            blu "你就是那个读着文字的玩家……"
            gre "嘘……有时这玩家读着屏幕上的一行行代码，将它们解码为文字；将文字解码为意义；将意义解码为感情、情绪、理论、想法，随后玩家的呼吸变快变深，他意识到了他还活着，他是活生生的，那上千次的死亡不是真的，玩家本身是活着的"
            blu "你。你。你是活着的。"
            gre "而有时这玩家相信，宇宙通过那缕穿越婆娑树影的夏日阳光对他说话"
            blu "有时这玩家相信，宇宙通过晴朗的冬日夜空中存在于他眼中一隅的星光对他说话。可能比太阳大上上百万倍的恒星将其行星烧成电浆，只为了让玩家在刹那间看到它。这时他在宇宙的远端，步行回家的路上，突然闻到食物的香味，快到那熟悉的门前，他又准备好再次入梦了"
            gre "而有时玩家相信宇宙通过“0”和“1”，通过世界的电力，通过屏幕上滚动的文字，在梦醒之前对他说话"
            blu "宇宙说，我爱你"
            gre "宇宙说，你精通这个游戏"
            blu "宇宙说，你所需的一切你都具有"
            gre "宇宙说，你比你所知的要强大"
            blu "宇宙说，你就是白昼"
            gre "宇宙说，你就是黑夜"
            blu "宇宙说，你所斗争的黑暗就在你心中"
            gre "宇宙说，你所追寻的光明就在你心中"
            blu "宇宙说，你并非孤身一人"
            gre "宇宙说，你并非与万物隔绝"
            blu "宇宙说，你就是宇宙本身，品尝着自己，对自己说话，阅读着自己的代码"
            gre "宇宙说，我爱你，因为你就是爱。"
            blu "曲终人散，黄粱一梦。玩家开始了新的梦境。玩家再次做起了梦，更好的梦。玩家就是宇宙。玩家就是爱。"
            blu "你就是那个玩家。"
            gre "醒来吧。"
            "游戏结束"
            "return"
            return
label integral:
    menu:
        "你要执行什么操作？"
        
        "查询积分":
            "你的积分是[persistent.integral]"
            jump integral
        "转出积分":
            python:
                try:
                    user_input = renpy.input("你要转出多少积分？", length=32)
                    if not user_input:
                        raise ValueError("输入为空") 
                    sz = int(user_input)
                    if sz <= 0:
                        narrator("转出数量必须大于0")
                    elif sz > persistent.integral:
                        narrator("余额不足")
                    else:
                        persistent.integral -= sz
                        code_val = pow(sz, 83, 8448)
                        narrator(f"请让对方输入：{code_val}")
                except ValueError:
                    narrator("输入无效，请输入数字")
                except Exception as e:
                    narrator(f"发生未知错误: {e}")
            jump integral
        "转入积分":
            python:
                try:
                    user_input = renpy.input("请输入对方发来的数字：", length=32)
                    if not user_input:
                        raise ValueError("输入为空")
                    sz = int(user_input)
                    if sz < 0 or sz >= 8448:
                        narrator("无效的验证码")
                    else:
                        sz = pow(sz, 987, 8448)
                        persistent.integral += sz
                        narrator(f"成功转入积分，当前积分：{persistent.integral}")
                except ValueError:
                    narrator("输入无效，请输入数字")
                except Exception as e:
                    narrator(f"发生未知错误: {e}")
            jump integral
        "返回主菜单":
            jump main