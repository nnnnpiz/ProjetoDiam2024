const FORM = document.getElementById('criar_conta');

    function check_str_for(str, test){
        for(c of str){
            if (test(c))
                return true;
        }
        return false;
    }

    const has_digit = password =>  check_str_for(password, (c) =>  '0' <=c && c <='9' );
    const has_upper = password =>  check_str_for(password, (c) => 'A' <= c && c <= 'Z' );
    const has_lower = password =>  check_str_for(password, (c) => 'a' <= c && c  <= 'z' );

    const symbols_allowed = {{ SYMBOLS_PASS }};
    const has_symbol = password => check_str_for(password, (c) => symbols_allowed.includes(c) );
    FORM.addEventListener('submit',
        event => {
            const password = document.getElementById('password_criar_conta_form').value
            const password_repited = document.getElementById('password-repitida').value
            const password_valid = password_repited === password &&
                password.length >= {{ PASSWORD_LEN }} &&
                has_upper(password) &&
                has_lower(password) &&
                has_symbol(password)  &&
                has_digit(password)
            if (!FORM.checkValidity() || !password_valid) {
                FORM.reportValidity()
                event.preventDefault()
                event.stopPropagation()
              }
        }, false)