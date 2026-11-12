#!/usr/bin/env python3
"""Builds index.html (the VietLish home page). The look, header and EN/VI switch are taken from privacy.html so the whole
site stays consistent. Run from the repository root:  python3 src/build_index.py"""
import re
from pathlib import Path
root = Path(__file__).resolve().parent.parent
priv = (root / 'privacy.html').read_text(encoding='utf8')
css = re.search(r'<style>(.*?)</style>', priv, re.S).group(1)
header = re.search(r'<header class="top">.*?</header>', priv, re.S).group(0)
header = header.replace(' aria-current="page"', '').replace('<a href="index.html"><span data-l="en">Home', '<a href="index.html" aria-current="page"><span data-l="en">Home', 1)
header = header.replace('<a class="brand" href="legal.html">', '<a class="brand" href="index.html">')
script = re.search(r'<script>.*?</script>', priv, re.S).group(0)
script = re.sub(r"  document\.querySelectorAll\('\.copy'\).*?\}\);\}\);\n", '', script, flags=re.S)

extra = '''
/* ---- Home page: gold and lucky red ---- */
body{background:radial-gradient(1200px 500px at 50% -120px,var(--accent-soft),transparent 70%),var(--bg)}
main{max-width:1040px}
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;padding:44px 0 12px}
.hero h1{font-size:clamp(36px,6vw,58px);line-height:1.05;letter-spacing:-1.2px;margin:0 0 14px}
.hero h1 em{font-style:normal;color:var(--accent)}
.hero p.lead{font-size:19px;color:var(--muted);max-width:560px;margin:0 0 22px}
.kicker{display:inline-block;background:var(--accent-soft);color:var(--accent);font-weight:700;font-size:13px;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:6px 14px;margin-bottom:16px;border:1px solid var(--gold)}
.stores{display:flex;flex-wrap:wrap;gap:10px}.store{display:inline-flex;flex-direction:column;border:1.5px solid var(--gold);background:var(--surface);color:var(--ink);border-radius:14px;padding:9px 20px;min-width:176px}
.store small{color:var(--muted);font-size:12px}.store b{font-size:17px}
.phone{position:relative;width:100%;max-width:300px;margin:0 auto;background:#2a1408;border-radius:42px;padding:10px;box-shadow:0 22px 50px rgba(120,60,0,.28),0 0 0 3px var(--gold)}
.phone img{display:block;width:100%;height:auto;border-radius:32px}
.phone.small{max-width:230px;border-radius:34px;padding:8px}.phone.small img{border-radius:26px}
section.block{padding:46px 0 0}
section.block h2{font-size:clamp(26px,4vw,34px);letter-spacing:-.6px;margin:0 0 6px}
section.block h2::after{content:"";display:block;width:56px;height:4px;border-radius:2px;background:linear-gradient(90deg,var(--gold),var(--accent));margin-top:10px}
.sub{color:var(--muted);margin:10px 0 0;max-width:640px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:20px 0 4px}
.tile{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--gold);border-radius:18px;padding:20px}
.tile h3{margin:0 0 6px;font-size:18px}.tile p{margin:0;color:var(--muted);font-size:15px}
.tile .big{font-size:32px;font-weight:800;letter-spacing:-.6px;color:var(--accent)}
.tile.best{background:linear-gradient(180deg,var(--accent-soft),var(--surface));border-color:var(--gold);box-shadow:0 10px 28px rgba(200,140,0,.2)}
.tile .tag{display:inline-block;background:var(--accent);color:var(--surface);font-size:12px;font-weight:700;border-radius:999px;padding:3px 10px;margin-bottom:8px}
.shots{display:flex;gap:22px;overflow-x:auto;padding:26px 4px 18px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}
.shot{flex:0 0 auto;scroll-snap-align:center;text-align:center;width:230px}.shot p{margin:14px 0 0;font-weight:700}.shot small{display:block;color:var(--muted);font-weight:400;font-size:14px;margin-top:2px}
.steps{counter-reset:s;list-style:none;padding:0;margin:20px 0}
.steps li{counter-increment:s;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 18px 14px 62px;margin:10px 0;position:relative}
.steps li::before{content:counter(s);position:absolute;left:16px;top:12px;width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--gold),var(--accent));color:#fff;display:grid;place-items:center;font-weight:800}
.topics{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin-top:20px}
.topic{background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}.topic img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover}
.topic p{margin:0;padding:10px 14px;font-weight:600;font-size:15px}.topic small{display:block;color:var(--muted);font-weight:400}
details{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:4px 18px;margin:10px 0}
summary{cursor:pointer;font-weight:700;padding:12px 0;list-style:none}summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;color:var(--accent);font-size:22px;line-height:1}details[open] summary::after{content:"\\2212"}
details p{margin:0 0 14px;color:var(--muted)}
.band{margin-top:46px;background:linear-gradient(135deg,#a51c1c,#7d1010);color:#fff3cf;border-radius:24px;padding:34px 28px;text-align:center;box-shadow:0 14px 34px rgba(120,10,10,.25);border:2px solid var(--gold)}
.band h2{margin:0 0 8px;font-size:clamp(24px,4vw,32px);color:#ffe08a}.band h2::after{display:none}.band p{margin:0 auto 18px;max-width:520px}
.band .store{background:#fff7e0;border-color:#ffe08a;color:#3a1c0e}.band .stores{justify-content:center}
.note{color:var(--muted);font-size:14px;margin-top:12px}
.foot{padding:30px 0 10px;color:var(--muted);font-size:14px;text-align:center}
@media (max-width:820px){.hero{grid-template-columns:1fr;padding-top:26px}.phone{max-width:260px}}
'''
def both(en, vi, tag='div'):
    return f'<{tag} data-l="en">{en}</{tag}>\n<{tag} data-l="vi">{vi}</{tag}>'
def sp(en, vi):
    return f'<span data-l="en">{en}</span><span data-l="vi">{vi}</span>'

TOPICS=[("Talking About Yourself","Giới thiệu về bản thân"),("Everyday Life","Cuộc sống hằng ngày"),("Keeping a Conversation Going","Giữ cuộc trò chuyện tiếp diễn"),("Talking About Experiences","Kể về trải nghiệm"),("Home and Responsibilities","Nhà cửa và trách nhiệm"),("Friends and Feelings","Bạn bè và cảm xúc"),("Work and Community","Công việc và cộng đồng"),("Expressing Yourself More Fully","Diễn đạt đầy đủ hơn")]
topics=''.join(f'<figure class="topic" style="margin:0"><img src="assets/topics/topic-{i+1}.jpg" alt="" loading="lazy" width="640" height="426"><p><small>{sp("Topic","Chủ đề")} {i+1}</small>{sp(e,v)}</p></figure>' for i,(e,v) in enumerate(TOPICS))
SHOTS=[("learn","Your lesson for today","Bài học hôm nay","One big card. Tap play.","Một thẻ lớn. Chạm để phát."),("player","A guided 20-minute lesson","Bài học 20 phút có hướng dẫn","Listen, build, recall, respond, converse.","Nghe, xây dựng, ôn, đáp lại, trò chuyện."),("practice","Practice what you learned","Luyện tập điều đã học","Flash cards, quick match, speak easy and more.","Thẻ từ, nối nhanh, nói dễ dàng và hơn thế nữa."),("paywall","Simple, fair pricing","Giá đơn giản, công bằng","Pick monthly or yearly. Cancel any time.","Chọn theo tháng hoặc năm. Hủy bất cứ lúc nào.")]
shots=''.join(f'<figure class="shot" style="margin:0 "><div class="phone small"><img src="assets/app/{n}.jpg" alt="VietLish screen: {te}" loading="lazy" width="760" height="1688"></div><p>{sp(te,tv)}<small>{sp(de,dv)}</small></p></figure>' for n,te,tv,de,dv in SHOTS)
FAQ=[("Is VietLish free?","VietLish có miễn phí không?","Lesson 1 of every mode and level is free. A VietLish subscription unlocks every lesson in Adults, Teens and Kids.","Bài 1 của mọi chế độ và cấp độ là miễn phí. Gói VietLish mở khóa mọi bài học Người lớn, Thiếu niên và Trẻ em."),
("How much does it cost?","Giá bao nhiêu?","99,000&#8363; a month or 999,000&#8363; a year (about 16% less). The store shows the exact price and billing period before you buy.","99.000&#8363; mỗi tháng hoặc 999.000&#8363; mỗi năm (rẻ hơn khoảng 16%). Cửa hàng hiển thị giá và chu kỳ thanh toán chính xác trước khi bạn mua."),
("Which phones does it work on?","Dùng được trên điện thoại nào?","Android and iPhone. The apps are coming soon.","Android và iPhone. Ứng dụng sắp ra mắt."),
("Is it Southern or Northern Vietnamese?","Là tiếng Việt miền Nam hay miền Bắc?","The course is written in Southern Vietnamese, and you can also choose Northern Vietnamese wording.","Khóa học viết bằng tiếng Việt miền Nam, và bạn cũng có thể chọn cách nói miền Bắc."),
("Can my children use it?","Con tôi có dùng được không?","Yes. Kids and Teens modes are made for use on a parent's device with a parent's permission. See our <a href='children.html'>Children page</a>.","Được. Chế độ Trẻ em và Thiếu niên dành cho việc dùng trên thiết bị của phụ huynh, với sự cho phép của phụ huynh. Xem <a href='children.html'>trang Trẻ em</a>."),
("How do I cancel or delete my account?","Làm sao hủy gói hoặc xóa tài khoản?","Cancel in Google Play or your Apple account settings. To delete your account, see <a href='delete-account.html'>Delete account</a>. Deleting your account does not cancel a subscription.","Hủy trong Google Play hoặc cài đặt tài khoản Apple. Để xóa tài khoản, xem <a href='delete-account.html'>Xóa tài khoản</a>. Xóa tài khoản không hủy gói đăng ký.")]
faq=''.join(f'<details><summary>{sp(qe,qv)}</summary><p>{sp(ae,av)}</p></details>' for qe,qv,ae,av in FAQ)
stores=f'<div class="stores" aria-label="Stores"><span class="store"><small>{sp("Coming soon on","Sắp có trên")}</small><b>Google Play</b></span><span class="store"><small>{sp("Coming soon on the","Sắp có trên")}</small><b>App Store</b></span></div>'

body = f'''<main>
<section class="hero">
<div>
<span class="kicker">{sp("Speak English or Vietnamese","Nói tiếng Anh hoặc tiếng Việt")}</span>
{both("<h1>Speak with <em>confidence.</em></h1><p class='lead'>Everyday conversations in Southern Vietnamese or English, twenty minutes at a time. Listen, repeat and answer out loud, one real-life lesson after another.</p>",
      "<h1>Tự tin <em>khi nói.</em></h1><p class='lead'>Hội thoại đời thường bằng tiếng Việt giọng miền Nam hoặc tiếng Anh, mỗi lần hai mươi phút. Nghe, nhắc lại và trả lời thành tiếng, từng bài học thực tế một.</p>")}
{stores}
<p class="note">{sp("Lesson 1 is free. No card needed to try it.","Bài 1 miễn phí. Không cần thẻ để dùng thử.")}</p>
</div>
<div class="phone"><img src="assets/app/learn.jpg" alt="VietLish home screen with today's lesson" width="760" height="1688"></div>
</section>

<section class="block" id="inside">
<h2>{sp("See inside the app","Xem bên trong ứng dụng")}</h2>
<p class="sub">{sp("Real screens from the VietLish app.","Màn hình thật từ ứng dụng VietLish.")}</p>
<div class="shots">{shots}</div>
</section>

<section class="block" id="why">
<h2>{sp("Why people like it","Vì sao mọi người thích")}</h2>
<div class="grid">
<div class="tile"><h3>{sp("You speak out loud","Bạn nói thành tiếng")}</h3><p>{sp("Not just tapping. Every lesson makes you say the words and answer in the pauses.","Không chỉ chạm màn hình. Mỗi bài học bắt bạn nói và đáp lại trong các khoảng nghỉ.")}</p></div>
<div class="tile"><h3>{sp("Real-life conversations","Hội thoại đời thường")}</h3><p>{sp("Meeting a neighbour, shopping, work, friends. Things you will really say.","Gặp hàng xóm, mua sắm, công việc, bạn bè. Những điều bạn thật sự sẽ nói.")}</p></div>
<div class="tile"><h3>{sp("Works with the screen locked","Chạy khi khóa màn hình")}</h3><p>{sp("Learn on a walk or in the car, with controls on the lock screen.","Học khi đi bộ hoặc trên xe, có nút điều khiển ở màn hình khóa.")}</p></div>
<div class="tile"><h3>{sp("One plan for the family","Một gói cho cả nhà")}</h3><p>{sp("Adults, teens and kids each keep their own profile and progress.","Người lớn, thiếu niên và trẻ em mỗi người có hồ sơ và tiến độ riêng.")}</p></div>
</div>
</section>

<section class="block" id="how">
<h2>{sp("How a lesson works","Một bài học diễn ra thế nào")}</h2>
<ol class="steps">
<li>{sp("<b>Hear</b> a short, complete conversation.","<b>Nghe</b> một đoạn hội thoại ngắn, trọn vẹn.")}</li>
<li>{sp("<b>Learn</b> the key expressions: meaning, words, syllables, and rebuilding each phrase from the end.","<b>Học</b> các cách nói chính: nghĩa, từ, âm tiết, và ghép lại từng câu từ cuối về đầu.")}</li>
<li>{sp("<b>Repeat</b> aloud, then <b>recall</b> earlier expressions.","<b>Nhắc lại</b> thành tiếng, rồi <b>ôn</b> những cách nói đã học.")}</li>
<li>{sp("<b>Respond</b> in the pauses, then play <b>both roles</b> in the full conversation.","<b>Trả lời</b> trong các khoảng nghỉ, rồi đóng <b>cả hai vai</b> trong hội thoại đầy đủ.")}</li>
</ol>
</section>

<section class="block" id="courses">
<h2>{sp("Eight topics, 32 lessons","Tám chủ đề, 32 bài học")}</h2>
<p class="sub">{sp("Learn English if you speak Vietnamese, or Vietnamese if you speak English. Adults get 20-minute lessons, teens 15, kids 10.","Học tiếng Anh nếu bạn nói tiếng Việt, hoặc học tiếng Việt nếu bạn nói tiếng Anh. Người lớn học 20 phút, thiếu niên 15 phút, trẻ em 10 phút.")}</p>
<div class="topics">{topics}</div>
</section>

<section class="block" id="price">
<h2>{sp("Simple pricing","Giá đơn giản")}</h2>
<div class="grid">
<div class="tile"><h3>{sp("Try it","Dùng thử")}</h3><div class="big">{sp("Free","Miễn phí")}</div><p>{sp("Lesson 1 of every mode and level.","Bài 1 của mỗi chế độ và cấp độ.")}</p></div>
<div class="tile"><h3>{sp("Monthly","Theo tháng")}</h3><div class="big">99.000&#8363;</div><p>{sp("per month. Every lesson in Adults, Teens and Kids.","mỗi tháng. Mọi bài học Người lớn, Thiếu niên và Trẻ em.")}</p></div>
<div class="tile best"><span class="tag">{sp("Best value","Tiết kiệm nhất")}</span><h3>{sp("Yearly","Theo năm")}</h3><div class="big">999.000&#8363;</div><p>{sp("per year. About 16% less than paying monthly.","mỗi năm. Rẻ hơn khoảng 16% so với trả theo tháng.")}</p></div>
</div>
<p class="note">{sp("Subscriptions renew until you cancel in Google Play or your Apple account settings. The price and billing period are shown in the store before you buy. On Android, free users can also watch one short ad a day to unlock one extra lesson for 24 hours.","Gói tự động gia hạn cho đến khi bạn hủy trong Google Play hoặc cài đặt tài khoản Apple. Giá và chu kỳ thanh toán hiển thị trong cửa hàng trước khi bạn mua. Trên Android, người dùng miễn phí cũng có thể xem một quảng cáo ngắn mỗi ngày để mở một bài học thêm trong 24 giờ.")}</p>
</section>

<section class="block" id="faq">
<h2>{sp("Questions","Câu hỏi thường gặp")}</h2>
{faq}
</section>

<section class="band">
<h2>{sp("Coming soon to your phone","Sắp có trên điện thoại của bạn")}</h2>
<p>{sp("VietLish is almost ready. Questions in the meantime? Write to us and we will answer.","VietLish sắp hoàn thiện. Có câu hỏi trong lúc chờ? Hãy viết cho chúng tôi, chúng tôi sẽ trả lời.")}</p>
{stores}
<p style="margin:16px 0 0"><b>appmakernguyen@gmail.com</b></p>
</section>

<p class="foot">© 2026 rubezapps · VietLish · <a href="privacy.html">{sp("Privacy","Quyền riêng tư")}</a> · <a href="terms.html">{sp("Terms","Điều khoản")}</a> · <a href="children.html">{sp("Children","Trẻ em")}</a> · <a href="delete-account.html">{sp("Delete account","Xóa tài khoản")}</a> · <a href="support.html">{sp("Support","Hỗ trợ")}</a></p>
</main>'''

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>VietLish · Speak English or Vietnamese</title>
<meta name="description" content="VietLish: speak English or Southern Vietnamese through short, real-life lessons. Courses for adults, teens and kids.">
<link rel="canonical" href="https://appmakernguyen-arch.github.io/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="VietLish · Speak English or Vietnamese">
<meta property="og:description" content="Short, real-life speaking lessons for adults, teens and kids. Listen, repeat and answer out loud.">
<meta property="og:image" content="https://appmakernguyen-arch.github.io/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap">
<style>{css}{extra}</style>
</head>
<body>
{header}
{body}
{script}
</body>
</html>
'''
(root / 'index.html').write_text(page, encoding='utf8')
print('wrote index.html', len(page), 'bytes')
