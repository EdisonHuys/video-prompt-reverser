# 影视复刻标准词汇表

反推时先识别属于哪一类，再把右侧措辞直接写进提示词。中英对照，通用版提示词可直接取用。拿不准时选更简单的词，不要堆砌术语。

## 1. 景别（Shot size）
| 术语 | 识别特征 | 提示词写法（中 / EN） |
|---|---|---|
| 大远景 Extreme long shot | 人物很小，环境为主 | 大远景，人物渺小 / extreme long shot, tiny figure in vast environment |
| 全景 Full shot | 人物全身入画，带周围环境 | 全景，人物全身 / full shot, full body |
| 中景 Medium shot | 膝盖/腰部以上 | 中景，腰部以上 / medium shot, waist up |
| 中近景 Medium close-up | 胸部以上 | 中近景，胸部以上 / medium close-up |
| 近景 Close-up | 肩部以上、脸为主 | 近景，面部为主 / close-up on face |
| 特写 Extreme close-up | 眼/嘴/手/物件局部 | 大特写，只取局部 / extreme close-up |

## 2. 机位角度（Camera angle）
| 术语 | 识别特征 | 提示词写法 |
|---|---|---|
| 平视 Eye-level | 镜头与眼同高 | 平视机位 / eye-level |
| 仰视 Low angle | 镜头低于主体向上拍，显高大 | 低角度仰拍 / low-angle shot looking up |
| 俯视 High angle | 镜头向下拍，显渺小 | 高角度俯视 / high-angle looking down |
| 侧面 Profile | 90° 侧脸 | 侧面轮廓 / profile view |
| 过肩 OTS | 越过一人肩膀拍另一人 | 过肩镜头 / over-the-shoulder |
| 主观 POV | 第一人称视角 | 主观视角 / POV first-person |
| 背后跟随 Back follow | 拍人物背影跟走 | 背后跟随 / following from behind |

## 3. 焦段与景深（Lens / DOF）
- 广角深景：环境清晰、边缘略变形 → `广角深景深，环境清晰 / wide lens, deep focus`
- 长焦浅景深：背景虚化光斑 → `长焦浅景深，背景虚化 / telephoto, shallow depth of field, blurred bokeh background`
- 标准自然：`标准焦段，自然透视 / natural standard lens`

## 4. 运镜（Camera movement）
| 术语 | 识别 | 提示词写法 |
|---|---|---|
| 固定 Static | 镜头不动 | 固定机位，镜头不动 / static locked-off camera |
| 推近 Push in | 向主体缓慢靠近，景别变大 | 缓慢匀速推近至近景 / slow steady push-in |
| 拉远 Pull out | 远离主体，环境展开 | 缓慢拉远 / slow pull-out |
| 摇 Pan/Tilt | 机位不动左右/上下摇 | 缓慢左摇 / slow pan left；上摇 tilt up |
| 横移 Track | 镜头平移跟主体 | 横向平移跟随 / lateral tracking shot |
| 跟随 Follow | 跟人一起走 | 平稳跟随人物 / smooth follow shot |
| 环绕 Orbit | 绕主体转圈 | 缓慢环绕半圈 / slow orbit around subject |
| 升降 Crane | 镜头升高/降低 | 缓慢升起 / slow crane up |
| 甩镜 Whip pan | 快速横甩带模糊 | 快速甩镜转场 / whip pan transition |
| 手持 Handheld | 轻微自然晃动 | 手持纪实，轻微晃动 / handheld documentary, slight shake |

## 5. 切镜与转场（Cut / Transition）
- 硬切 Hard cut：直接跳下一镜 → 提示词写"硬切"，剪辑后期处理。
- 动作中切 Action cut：在动作进行中切到下一角度。
- 视线切 Look cut：顺着人物视线切到所看对象。
- 反应切 Reaction cut：切到听者/旁观者表情。
- 遮挡切 Wipe/occlusion：被人或物体挡满画面后切。
- 叠化 Dissolve：两镜交叉淡化（抒情/时间流逝）。
- 淡入淡出 Fade to black。
- 匹配剪辑 Match cut：相似形状/动作相接。
> 文生单条只复现镜内运动；切镜、叠化、甩镜由后期剪辑完成，提示词里标注"切镜后期"。

## 6. 表情（Expression，写到眉眼嘴）
- 平静垂目：`眼神低垂，表情平静，嘴唇轻闭`
- 轻笑：`嘴角微微上扬，浅笑，眼神柔和`
- 开怀笑：`露齿大笑，眼睛弯起`
- 惊讶：`眼睛睁大，嘴微张，眉毛抬起`
- 落寞疏离：`眼神放空，面无表情，视线落向一侧`
- 温柔注视：`目光柔和看向对方，嘴角带笑`

## 7. 动作姿态（Action）
- 静立：`双手插兜，自然站立，轻微呼吸起伏`
- 转身：`先侧脸，随后转身背对镜头向右离开`
- 行走：`背向镜头缓步走向远处，步伐从容`
- 抬手：`一只手缓缓向上抬起，伸向夜空`
- 甩发：`头部轻甩，长发随之扬起再落下`
- 靠近：`两人面对面缓慢靠近，目光相对`

## 8. 光线（Lighting）
- 侧光：`主光从左侧打来，脸部一半受光`
- 逆光：`身后逆光勾出发丝轮廓 / backlight rim light`
- 顶光：`顶部冷白圆形顶灯直射 / cool overhead top light`
- 霓虹/招牌光：`红色发光招牌从正面打暖红光`
- 环境光斑：`远处车尾灯虚化成暖色光斑`

## 9. 调色与风格（Grade / Look）
- 夜街纪实暖调：`夜晚手持纪实，低饱和暖黄与招牌红光，暗部偏冷青，轻微胶片颗粒`
- 冷青电梯：`冷青白顶光，绿色镜面反射，低饱和`
- 青橙电影感：`青橙调色，暗部偏青、高光偏橙`
- 复古胶片：`复古胶片，柔和对比，细腻颗粒，暖褪色`
- 清新自然光：`柔和自然散射光，高明度低对比`

## 10. 声音（Sound）
- 对白：`人物对白（角色）：{逐字原文}`，标注情绪语速。
- BGM：写明曲风、节拍、是否卡点；MV 写歌词逐字。
- 环境声：车流/脚步/电梯提示音/风声；无人声时写"氛围环境声，无人声对白"。
