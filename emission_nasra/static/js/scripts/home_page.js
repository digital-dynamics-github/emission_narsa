import invock, {Component} from "invock-js";
import Plugins from "../plugins/plugins";

class HomePage extends Component {
    constructor(params) {
        super(params);
        this.ref_uid = "uid_ref_narsa_2021";
        
        this.events = {
            "click .vote-btn" : "applyVote"
        }
        
    }
    
    applyVote(evt, self) {
        var uid_candidat = this.data("uid");
        var class_disabled = this.hasClass("disabled");
        
        if ( class_disabled === false ) {
            var state_person = self.verifyperson();
           if ( state_person === false ) {
               var parent = dom.get("#prepend-body");

               self.renderOtherComponent("PopupPerson", { "uid" : uid_candidat }, parent, null);
           }
        }
        else {
            
        }
        
        
    }
    
    
    verifyperson(){
        var object_uid_person = null;
        var state = false;
        if (typeof(Storage) !== "undefined") {
            if ( localStorage.length > 0 ) {
                object_uid_person = localStorage.uid_ref_narsa_2021;
            }
        }
        
        
        if (object_uid_person !== null) {
            state = true;
        }
        
        return state;
        
    }
    
    afterRender() {
        
        this.verifyVote();
        
        
    }

    verifyVote() {
        var state_person = this.verifyperson();
        
        if ( state_person === true ) {
            var btns_votes = dom.getAll(".vote-btn");
            if (btns_votes.length > 0) {
                btns_votes.addClass("disabled");
                console.log("0000");
            }
        }
    }
    
}


class PopupPerson extends Component {
    
    constructor(params) {
        super(params);
        
        this.events = {
            "click .action-popup" : "actionPopup"
            
        }
    }
    
    afterRender() {
         dom.get(".overlay-popup").animate(0.5, { "opacity" : 1});
    }
    
    close() {
        var self = this;
        dom.get(".overlay-popup").animate(0.5, { "opacity" : 0, onComplete : function() {
                dom.get(".overlay-popup").remove();
            } 
        });
        
        dom.get(".container-popup").animate(0.5, { "opacity" : 0, onComplete : function() {
                dom.get(".container-popup").remove();
            } 
        });
        
        dom.removeCallScroll( this.name);
        
    }
    
    saveUidRef(uid_ref) {
        if (typeof(Storage) !== "undefined") {
            if ( localStorage.length === 0 && uid_ref !== null && typeof uid_ref !== "undefined") {
                localStorage.setItem("uid_ref_narsa_2021", uid_ref);
            }
        }
    }
    
    actionPopup(evt, self) {
        var action = this.data("action");
        
        if (action === "close") {
            self.close();
        }    
        
        if ( action === "save" ) {
            var form = self.parent.find("form");
            
            form.runPlugin("validator", {
                parent : form,
                valid : function(response, s, n , t) {
                    if (response) {
                       var serialize = form.serialize("object");
                        var url = "/api/site/save-person/";
                        self.http.url = url;
                        self.http.post(serialize, function(response) {
                           if ( response.status === "success" ) {
                               var uid_ref = response.uid_ref;
                               self.saveUidRef(response.uid_ref);
                               self.renderOtherComponent("Message", { "message" : response.message, "status" : response.status }, dom.get("#prepend-body"), null);
                           }
                        });
                    }
                },
                error : function() {
                    evt.preventDefault();
                    return false;
                }
            });
        }
    }
    
    
    
    render() {
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Votez et participez automatiquement à la TOMBOLA</h2>
                    <form id="form-person">
                        <input type="hidden" name="candidat" value="{{props.uid}}" />
                        <p>
                            <label>Nom complet <span class="asterix">*</span></label>
                            <input type="text" name="name" placeholder="Example : Mohamed hassan" class="required" data-rule="string" />
                        </p>
                        
                        <p>
                            <label>Adresse email</label>
                            <input type="text" name="email" placeholder="Example : example@example.com" class="required" data-rule="email" />
                        </p>

                        <p>
                            <label>Numéro du téléphone <span class="asterix">*</span></label>
                            <input type="text" name="phone" placeholder="Example : 0666666666" class="required" data-rule="string" />
                        </p>

                        <p class="relative">
                            <input type="checkbox" name="accept_reglement" class="required" data-rule="boolean" />
                            <label>j'accepte <a href="/reglements/" target="_blank" class="bleu-color souligner">les réglements du TOMBOLA</a></label>
                            
                        </p>
                        
                        <p>
                            <span class="asterix">*</span> <span> : Champs obligatoires</span>
                        </p>

                        <div class="align-center top30">
                            <input type="button" value="Annuler" class="action-popup btn gris" data-action="close" />
                            <input type="button" value="Votez" class="action-popup btn bleu" data-action="save" />
                        </div>
                        
                    </form>
                
                </div>
            </div>
      `; 
    }
}



class Message extends Component {
    
    constructor(params) {
        super(params);
    }
    
    afterRender() {
        var self = this;
         dom.get(".overlay-popup").animate(0.5, { "opacity" : 1});
        var timer = setTimeout(function() {
            
            self.close();
            
        }, 4000);
    }
    
    close() {
        var self = this;
        dom.get(".overlay-popup").animate(0.5, { "opacity" : 0, onComplete : function() {
                dom.get(".overlay-popup").remove();
            } 
        });
        
        dom.get(".container-popup").animate(0.5, { "opacity" : 0, onComplete : function() {
                dom.get(".container-popup").remove();
            } 
        });
        
        dom.removeCallScroll( this.name);
        
    }
    
    
    
    
    
    render() {
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-message relative {{props.status}}">{{props.message}}</div>
            </div>
      `; 
    }
}




invock.export("Message", Message);
invock.export("PopupPerson", PopupPerson);

invock.export("HomePage", HomePage);
invock.mount({ parent : "body", root : "{% HomePage parent_name='body' %}" });