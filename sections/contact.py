import streamlit as st

def render_contact():
    st.markdown("""
    <div id="contact" class="contact-section-box">
        <div class="contact-title" style="margin-bottom:2.2rem;">📞 Contact Me</div>
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