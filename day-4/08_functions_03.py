def verify_otp(prompt, max_attempts=3, error_msg="Invalid OTP, try again!"):
    correct_otp = "1234"

    while max_attempts > 0:
        entered_otp = input(prompt)

        if entered_otp == correct_otp:
            print("OTP verified successfully ✅")
            return True

        max_attempts -= 1
        print(error_msg)

    print("OTP blocked 🚫 Too many attempts")
    return False

# verify_otp("Enter OTP: ")
verify_otp(
    prompt="Enter OTP sent to your phone: ",
    max_attempts=1,
    error_msg="Last chance 😬"
)
