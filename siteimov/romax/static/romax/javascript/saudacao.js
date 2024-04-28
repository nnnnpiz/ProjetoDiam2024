function dar_dia_tarde_ou_noite() {
                            /*
                               Method responsible for deciding if to say
                               "Bom dia", "Boa tarde" or "Boa noite"
                                depending on user local hour!!
                             */
                            //TODO corrigir qnd é periodo do dia, tarde, noite
                            function between(n, min, max) {
                                return min <= n && n < max;
                            }
                            const curr_hora = new Date().getHours();
                            if (between(curr_hora, 6, 12))
                                return "Bom dia"
                            else if (between(curr_hora, 12, 20))
                                return 'Boa tarde'
                            else
                                return "Boa noite"
                        }
                        document.getElementById("welcome_msg").innerText = `${dar_dia_tarde_ou_noite()},` + ' 1º e ultimo nome ' + `estamos gratos de o ver novamente!`