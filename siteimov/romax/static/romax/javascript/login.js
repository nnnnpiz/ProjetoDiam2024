const LOGIN_FORM = document.getElementById('login-form');
                function create_payload(){
                    let out = '';
                    const FORM_DATA = Object.fromEntries(new FormData(LOGIN_FORM));
                    for(key in FORM_DATA){
                        out += `${key}=${FORM_DATA[key]}&`
                    }
                    return out;
                }
                LOGIN_FORM.addEventListener('submit',
                    event => {
                            event.preventDefault();
                            event.stopPropagation();
                            if (LOGIN_FORM.checkValidity()) {
                                $.ajax({
                                    url: LOGIN_FORM.action,
                                    dataType: 'text',
                                    type: 'post',
                                    data: create_payload(),
                                    statusCode: {
                                    401: function() {
                                       document.getElementById('msg-email-pass-invalidas').hidden = false;
                                    }
                                  },
                                'success': function(response){
                                   window.location.href=response;
                               }
                                });
                            }
                        }, false)