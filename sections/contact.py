import streamlit as st

def render_contact():
    st.markdown("""
    <style>
    .contact-section {
        margin: 0 auto 36px auto;
        max-width: 900px;
        width: 100%;
        background: rgba(20, 18, 38, 0.82);
        border-radius: 24px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        padding: 36px 48px 28px 48px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        font-size: 0.82em;           /* Decreased font size */
        font-weight: 200;
        line-height: 1.7;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        border: 2.5px solid #c471f5;
        z-index: 2;
        animation: fade-in-up 1s ease-out 2.2s forwards;
        opacity: 0;
    }
    .contact-title {
        font-size: 1.7em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 18px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
        margin-left: auto;
        margin-right: auto;
    }
    .contact-form {
        width: 100%;
        max-width: 750px; /* Make the form itself wide */
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .contact-form label {
        font-weight: 600;
        color: #00e6ff;
        margin-bottom: 6px;
        display: block;
        text-align: left;
        width: 100%;
        max-width: 700px;
        font-size: 1.15em;   /* Increased label font size for sub-headings */
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        max-width: 700px; /* Make fields wide */
        padding: 16px;
        margin-bottom: 24px;
        border-radius: 12px;
        border: none;
        background: #f3eaff;
        color: #222;
        font-size: 0.87em;           /* Decreased input font size */
        font-family: inherit;
        outline: none;
        transition: box-shadow 0.2s;
        box-shadow: 0 2px 8px #c471f555;
        resize: none;
        box-sizing: border-box;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .contact-form textarea {
        min-height: 140px;
        max-height: 320px;
    }
    .contact-form button {
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        color: #fff;
        border: none;
        border-radius: 10px;
        padding: 12px 32px;
        font-size: 0.87em;           /* Decreased button text size */
        font-weight: 400;
        cursor: pointer;
        transition: background 0.2s, transform 0.2s;
        box-shadow: 0 2px 8px #c471f555;
        margin-top: 8px;
        min-width: 180px;
        max-width: 300px;
    }
    .contact-form button:hover {
        background: linear-gradient(90deg, #c471f5 0%, #00e6ff 100%);
        transform: scale(1.04);
    }
    .contact-success {
        color: #00e6ff;
        font-weight: 700;
        margin-top: 18px;
        font-size: 0.85em;           /* Decreased success message size */
        text-align: center;
    }
    @media (max-width: 900px) {
        .contact-section {
            max-width: 98vw;
            padding: 24px 2vw 24px 2vw;
        }
        .contact-form, .contact-form input, .contact-form textarea {
            max-width: 98vw;
        }
    }
    @media (max-width: 700px) {
        .contact-section {
            padding: 18px 2vw 18px 2vw;
        }
        .contact-title {
            font-size: 1.1em;
            padding: 0.2rem 0.7rem;
        }
        .contact-form, .contact-form input, .contact-form textarea {
            max-width: 100vw;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div id="contact" class="contact-section">
        <div class="contact-title">📬 Contact Me</div>
        <form class="contact-form" id="contact-form">
            <label for="name">Name</label>
            <input type="text" id="name" name="user_name" required placeholder="Your Name" />
            <label for="email">Email</label>
            <input type="email" id="email" name="user_email" required placeholder="your@email.com" />
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="5" required placeholder="Type your message..."></textarea>
            <button type="submit">Send</button>
        </form>
        <div id="contact-success" class="contact-success"></div>
    </div>
    """, unsafe_allow_html=True)

    # EmailJS integration (replace YOUR_SERVICE_ID, YOUR_TEMPLATE_ID, YOUR_PUBLIC_KEY)
    st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/emailjs-com@3/dist/email.min.js"></script>
    <script>
    (function(){
        emailjs.init("1lJLdVfGcU1KdOtki "); // <-- Replace with your real public key!
    })();
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        emailjs.sendForm('service_bqqdkpj', 'template_v1mwfrh', this)
            .then(function() {
                document.getElementById('contact-success').innerHTML = "Thank you! Your message has been sent.";
                document.getElementById('contact-form').reset();
            }, function(error) {
                document.getElementById('contact-success').innerHTML = "Oops! Something went wrong. Please try again.";
            });
    });
    </script>
    """, unsafe_allow_html=True)