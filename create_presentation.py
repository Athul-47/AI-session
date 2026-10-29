import os
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(OUTPUT_DIR, "presentation_assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_font(size, bold=False, italic=False):
    fonts = [
        "C:\\Windows\\Fonts\\georgiab.ttf" if bold and not italic else
        "C:\\Windows\\Fonts\\georgiaz.ttf" if bold and italic else
        "C:\\Windows\\Fonts\\georgiai.ttf" if italic else
        "C:\\Windows\\Fonts\\georgia.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
    ]
    for font_path in fonts:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def create_app_mockup():
    w, h = 950, 600
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([15, 15, w-15, h-15], radius=24, fill=(230, 239, 248, 255), outline=(200, 215, 230, 255), width=2)
    draw.rounded_rectangle([50, 45, w-50, h-45], radius=20, fill=(255, 255, 255, 255), outline=(220, 230, 240, 255), width=2)

    f_title = get_font(22, bold=True)
    draw.text((90, 80), "Quote of the day", fill=(75, 90, 120), font=f_title)

    f_quote = get_font(34, italic=True)
    draw.text((90, 150), "“Start where you are.", fill=(20, 33, 61), font=f_quote)
    draw.text((90, 200), " Use what you have.", fill=(20, 33, 61), font=f_quote)
    draw.text((90, 250), " Do what you can.”", fill=(20, 33, 61), font=f_quote)

    f_author = get_font(24, bold=True)
    draw.text((90, 330), "— Arthur Ashe", fill=(75, 90, 120), font=f_author)

    btn_y = 410
    draw.rounded_rectangle([90, btn_y, 350, btn_y + 80], radius=40, fill=(255, 255, 255), outline=(20, 33, 61), width=3)
    draw.ellipse([105, btn_y + 12, 160, btn_y + 67], fill=(255, 183, 3), outline=(231, 157, 0), width=3)
    
    f_btn = get_font(26, bold=True)
    draw.text((180, btn_y + 24), "New quote", fill=(20, 33, 61), font=f_btn)

    path = os.path.join(ASSETS_DIR, "app_mockup.png")
    img.save(path, "PNG")
    return path

def create_routine_gap_card():
    w, h = 900, 520
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([10, 10, w-10, h-10], radius=20, fill=(255, 255, 255, 255), outline=(225, 235, 242, 255), width=2)

    f_card_title = get_font(24, bold=True)
    draw.text((50, 40), "THE MORNING ROUTINE GAP", fill=(40, 80, 60), font=f_card_title)
    
    f_sub = get_font(18, italic=True)
    draw.text((50, 75), "How your first 5 minutes shape the rest of your day", fill=(100, 115, 130), font=f_sub)

    draw.rounded_rectangle([50, 125, 420, 460], radius=16, fill=(254, 242, 242), outline=(252, 165, 165), width=2)
    f_h2 = get_font(20, bold=True)
    draw.text((75, 150), "❌ The Digital Scroll", fill=(185, 28, 28), font=f_h2)

    f_body = get_font(17)
    items_neg = [
        "• Wake up to stress alerts",
        "• Endless news & doomscrolling",
        "• Comparison & scattered mind",
        "• Reactionary, hurried start"
    ]
    y = 205
    for item in items_neg:
        draw.text((75, y), item, fill=(127, 29, 29), font=f_body)
        y += 48

    draw.rounded_rectangle([460, 125, 840, 460], radius=16, fill=(240, 253, 244), outline=(134, 239, 172), width=2)
    draw.text((485, 150), "✅ The Mindful Reset", fill=(21, 128, 61), font=f_h2)

    items_pos = [
        "• One intentional thought",
        "• Grounded Stoic wisdom",
        "• Deep calm & clarity",
        "• Focus on what you control"
    ]
    y = 205
    for item in items_pos:
        draw.text((485, y), item, fill=(20, 83, 45), font=f_body)
        y += 48

    path = os.path.join(ASSETS_DIR, "routine_gap.png")
    img.save(path, "PNG")
    return path

def create_closing_card():
    w, h = 900, 420
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([10, 10, w-10, h-10], radius=24, fill=(24, 44, 34), outline=(45, 85, 65), width=2)

    f_glyph = get_font(80, italic=True)
    draw.text((60, 40), "“", fill=(255, 183, 3), font=f_glyph)

    f_quote = get_font(30, italic=True)
    draw.text((80, 130), "Courage is taking the next step,", fill=(255, 255, 255), font=f_quote)
    draw.text((80, 180), "even when you are unsure.", fill=(255, 255, 255), font=f_quote)

    f_author = get_font(24, bold=True)
    draw.text((80, 260), "— Mary Anne Radmacher", fill=(255, 183, 3), font=f_author)

    f_status = get_font(18)
    draw.text((80, 340), "✨ Full Stack Python App • Ready for daily motivation", fill=(160, 190, 175), font=f_status)

    path = os.path.join(ASSETS_DIR, "closing_card.png")
    img.save(path, "PNG")
    return path

def build_presentation():
    app_mockup_path = create_app_mockup()
    routine_gap_path = create_routine_gap_card()
    closing_card_path = create_closing_card()

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    DARK_GREEN = RGBColor(22, 42, 32)
    LIGHT_BG = RGBColor(248, 250, 249)
    WHITE = RGBColor(255, 255, 255)
    GOLD = RGBColor(255, 183, 3)
    MUTED_SLATE = RGBColor(140, 160, 150)
    DARK_TEXT = RGBColor(20, 33, 61)
    BODY_TEXT = RGBColor(70, 85, 105)

    def add_full_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    # Slide 1
    s1 = prs.slides.add_slide(blank_layout)
    add_full_bg(s1, DARK_GREEN)

    tb1 = s1.shapes.add_textbox(Inches(0.9), Inches(1.1), Inches(6.5), Inches(5.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p_tag = tf1.paragraphs[0]
    p_tag.text = "PROJECT PRESENTATION • OCTOBER 2026"
    p_tag.font.size = Pt(12)
    p_tag.font.bold = True
    p_tag.font.color.rgb = GOLD
    p_tag.space_after = Pt(24)

    p_title = tf1.add_paragraph()
    p_title.text = "Quote of the Day"
    p_title.font.size = Pt(46)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE
    p_title.space_after = Pt(18)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Start each morning with clarity and intent — one simple click for timeless wisdom, perspective, and daily focus."
    p_sub.font.size = Pt(17)
    p_sub.font.color.rgb = RGBColor(210, 225, 215)
    p_sub.space_after = Pt(28)

    p_pills = tf1.add_paragraph()
    p_pills.text = "Python (Flask)   •   HTML5 & CSS3   •   JavaScript   •   REST API"
    p_pills.font.size = Pt(13)
    p_pills.font.bold = True
    p_pills.font.color.rgb = GOLD
    p_pills.space_after = Pt(36)

    p_tagline = tf1.add_paragraph()
    p_tagline.text = "one click. A little more inspiration."
    p_tagline.font.size = Pt(15)
    p_tagline.font.italic = True
    p_tagline.font.color.rgb = MUTED_SLATE

    p_author = tf1.add_paragraph()
    p_author.text = "Presenter: Athul"
    p_author.font.size = Pt(13)
    p_author.font.color.rgb = MUTED_SLATE

    s1.shapes.add_picture(app_mockup_path, Inches(7.4), Inches(1.2), width=Inches(5.0))

    # Slide 2
    s2 = prs.slides.add_slide(blank_layout)
    add_full_bg(s2, LIGHT_BG)

    tb2 = s2.shapes.add_textbox(Inches(0.9), Inches(0.8), Inches(6.0), Inches(5.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p2_tag = tf2.paragraphs[0]
    p2_tag.text = "01 | THE PROBLEM"
    p2_tag.font.size = Pt(12)
    p2_tag.font.bold = True
    p2_tag.font.color.rgb = RGBColor(20, 100, 60)
    p2_tag.space_after = Pt(12)

    p2_title = tf2.add_paragraph()
    p2_title.text = "Digital noise drains daily motivation"
    p2_title.font.size = Pt(34)
    p2_title.font.bold = True
    p2_title.font.color.rgb = DARK_TEXT
    p2_title.space_after = Pt(24)

    points = [
        ("Mornings set the tone: ", "How we start our first 10 minutes dictates stress levels, focus, and productivity for the day."),
        ("Notification overload: ", "People wake up straight to emails, social feeds, and sensory fatigue."),
        ("Cluttered alternatives: ", "Existing quote websites are packed with intrusive ads, paywalls, and anonymous quotes."),
        ("The mindful reset: ", "A clean, distraction-free space to ground your mindset in under 5 seconds.")
    ]

    for bold_prefix, text in points:
        p = tf2.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + bold_prefix
        r1.font.bold = True
        r1.font.size = Pt(15)
        r1.font.color.rgb = DARK_TEXT

        r2 = p.add_run()
        r2.text = text
        r2.font.size = Pt(15)
        r2.font.color.rgb = BODY_TEXT
        p.space_after = Pt(14)

    s2.shapes.add_picture(routine_gap_path, Inches(7.2), Inches(1.3), width=Inches(5.3))

    # Slide 3
    s3 = prs.slides.add_slide(blank_layout)
    add_full_bg(s3, LIGHT_BG)

    tb3_h = s3.shapes.add_textbox(Inches(0.9), Inches(0.8), Inches(11.5), Inches(1.5))
    tf3_h = tb3_h.text_frame
    tf3_h.word_wrap = True

    p3_tag = tf3_h.paragraphs[0]
    p3_tag.text = "02 | THE SOLUTION"
    p3_tag.font.size = Pt(12)
    p3_tag.font.bold = True
    p3_tag.font.color.rgb = RGBColor(20, 100, 60)
    p3_tag.space_after = Pt(8)

    p3_title = tf3_h.add_paragraph()
    p3_title.text = "Simple, intentional, and inspiring"
    p3_title.font.size = Pt(34)
    p3_title.font.bold = True
    p3_title.font.color.rgb = DARK_TEXT

    card_w = Inches(3.65)
    card_h = Inches(4.3)
    card_y = Inches(2.2)

    cards_data = [
        ("🏛️ Timeless Wisdom", "Curated collection of profound insights spanning stoicism, mindfulness, creativity, and perseverance.\n\nNo generic fluff — thoughts that give real emotional grounding.", Inches(0.9)),
        ("✍️ Authentic Attribution", "Every single quote credits the philosopher, athlete, author, or leader who said it.\n\nDisplays author name clearly beneath the quote with a gentle fade transition.", Inches(4.85)),
        ("🔄 Anti-Repeat Engine", "Built-in randomization algorithm prevents consecutive duplicate quotes.\n\nGuarantees fresh inspiration every time you click the morning sun.", Inches(8.8))
    ]

    for title, body, card_x in cards_data:
        shape = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_x, card_y, card_w, card_h)
        shape.fill.solid()
        shape.fill.fore_color.rgb = WHITE
        shape.line.color.rgb = RGBColor(220, 230, 238)
        shape.line.width = Pt(1.5)

        tf_c = shape.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.3)
        tf_c.margin_right = Inches(0.3)
        tf_c.margin_top = Inches(0.4)

        p_ct = tf_c.paragraphs[0]
        p_ct.text = title
        p_ct.font.size = Pt(20)
        p_ct.font.bold = True
        p_ct.font.color.rgb = DARK_TEXT
        p_ct.space_after = Pt(18)

        p_cb = tf_c.add_paragraph()
        p_cb.text = body
        p_cb.font.size = Pt(15)
        p_cb.font.color.rgb = BODY_TEXT

    # Slide 4
    s4 = prs.slides.add_slide(blank_layout)
    add_full_bg(s4, LIGHT_BG)

    tb4_h = s4.shapes.add_textbox(Inches(0.9), Inches(0.8), Inches(11.5), Inches(1.5))
    tf4_h = tb4_h.text_frame
    tf4_h.word_wrap = True

    p4_tag = tf4_h.paragraphs[0]
    p4_tag.text = "03 | TECHNICAL ARCHITECTURE"
    p4_tag.font.size = Pt(12)
    p4_tag.font.bold = True
    p4_tag.font.color.rgb = RGBColor(20, 100, 60)
    p4_tag.space_after = Pt(8)

    p4_title = tf4_h.add_paragraph()
    p4_title.text = "Lightweight Python engine, responsive frontend"
    p4_title.font.size = Pt(34)
    p4_title.font.bold = True
    p4_title.font.color.rgb = DARK_TEXT

    step_w = Inches(3.65)
    step_h = Inches(4.3)
    step_y = Inches(2.2)

    steps_data = [
        ("Step 1: The Morning Sun", "User clicks the sun button.\n\n• Smooth CSS rotation on hover\n• Keyboard spacebar shortcut\n• Instant response without page reloads", Inches(0.9)),
        ("Step 2: Flask REST API", "Asynchronous GET /api/quote.\n\n• Python randomly selects quote\n• Avoids last_quote duplication\n• Returns JSON {quote, author}", Inches(4.85)),
        ("Step 3: Gentle Reveal", "Client DOM updates seamlessly.\n\n• Text updated via JavaScript\n• CSS keyframe fade animation\n• Author credit displayed below", Inches(8.8))
    ]

    for title, body, step_x in steps_data:
        shape = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, step_x, step_y, step_w, step_h)
        shape.fill.solid()
        shape.fill.fore_color.rgb = WHITE
        shape.line.color.rgb = RGBColor(220, 230, 238)
        shape.line.width = Pt(1.5)

        tf_s = shape.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = Inches(0.3)
        tf_s.margin_right = Inches(0.3)
        tf_s.margin_top = Inches(0.4)

        p_st = tf_s.paragraphs[0]
        p_st.text = title
        p_st.font.size = Pt(20)
        p_st.font.bold = True
        p_st.font.color.rgb = RGBColor(20, 100, 60)
        p_st.space_after = Pt(18)

        p_sb = tf_s.add_paragraph()
        p_sb.text = body
        p_sb.font.size = Pt(15)
        p_sb.font.color.rgb = BODY_TEXT

    # Slide 5
    s5 = prs.slides.add_slide(blank_layout)
    add_full_bg(s5, LIGHT_BG)

    tb5 = s5.shapes.add_textbox(Inches(0.9), Inches(0.8), Inches(6.0), Inches(5.8))
    tf5 = tb5.text_frame
    tf5.word_wrap = True

    p5_tag = tf5.paragraphs[0]
    p5_tag.text = "04 | IMPACT & CONCLUSION"
    p5_tag.font.size = Pt(12)
    p5_tag.font.bold = True
    p5_tag.font.color.rgb = RGBColor(20, 100, 60)
    p5_tag.space_after = Pt(12)

    p5_title = tf5.add_paragraph()
    p5_title.text = "Small steps every day add up to big changes"
    p5_title.font.size = Pt(32)
    p5_title.font.bold = True
    p5_title.font.color.rgb = DARK_TEXT
    p5_title.space_after = Pt(24)

    takeaways = [
        ("Clean Full-Stack Flow: ", "Seamless connection between a Python web service and a responsive UI."),
        ("Credible Motivation: ", "Adding the author makes each quote authentic and thought-provoking."),
        ("Fast & Distraction-Free: ", "Zero bloat, under 100ms response time, accessible on any device."),
        ("Ready for Future: ", "Easily expandable with categories, speech synthesis, and dark mode.")
    ]

    for bold_prefix, text in takeaways:
        p = tf5.add_paragraph()
        r1 = p.add_run()
        r1.text = "✔ " + bold_prefix
        r1.font.bold = True
        r1.font.size = Pt(15)
        r1.font.color.rgb = DARK_TEXT

        r2 = p.add_run()
        r2.text = text
        r2.font.size = Pt(15)
        r2.font.color.rgb = BODY_TEXT
        p.space_after = Pt(14)

    s5.shapes.add_picture(closing_card_path, Inches(7.2), Inches(1.5), width=Inches(5.3))

    pptx_path = os.path.join(OUTPUT_DIR, "Quote-of-the-Day-Presentation.pptx")
    prs.save(pptx_path)

if __name__ == "__main__":
    build_presentation()

