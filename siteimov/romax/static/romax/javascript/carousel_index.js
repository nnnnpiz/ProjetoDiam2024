let first_showed = 0;
                let last_showed = HOW_MANY_AT_A_TIME - 1;

                setInterval(on_click_right_button, SHIFT_PERIOD);

                for(let i = 0; i < HOW_MANY_AT_A_TIME; i++){
                    CARROSSEL.appendChild(CARROSSEL_ELEM_LIST[i])
                }

                 function on_click_left_button(){
                    first_showed=--first_showed >= 0? first_showed: HOW_MANY_TOTAL - 1
                     console.log(CARROSSEL_ELEM_LIST.length)
                     CARROSSEL.prepend(CARROSSEL_ELEM_LIST[first_showed])
                     CARROSSEL.removeChild(CARROSSEL.lastChild)
                     //TODO fix line above
                    last_showed=  --last_showed >= 0? last_showed: HOW_MANY_TOTAL - 1
                }
                function on_click_right_button(){
                     first_showed= ++first_showed < HOW_MANY_TOTAL? first_showed : 0
                     last_showed= ++last_showed < HOW_MANY_TOTAL? last_showed : 0
                     CARROSSEL.removeChild(CARROSSEL.firstChild)
                     CARROSSEL.append(CARROSSEL_ELEM_LIST[last_showed])
                }