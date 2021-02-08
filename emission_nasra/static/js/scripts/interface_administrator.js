import invock, {Component} from "invock-js";
import Plugins from "../plugins/plugins";

class InterfaceAdministrator extends Component {
    constructor(params) {
        super(params);
        
        this.events = {
            "click .widget-switch" : "changeStateSwitch",
            "click .add-widget" : "addWidget",
            "click #create-reglement" : "createReglement",
            "click #update-reglement" : "updateReglement",
        }
        
    }
    
    
    updateReglement(evt, self) {
        var uid = this.data("id");
        
        var url = "/api/site/get-reglement/"+uid+"/";
        self.http.url = url;
        self.http.fetch(function(response) {
            if ( response.data !== null ) {
                var parent = dom.get("#prepend-body");
                self.renderOtherComponent("PopupReglement", { "action" : "update", "uid" : uid, "title" : response.data.title, "content" : response.data.content }, parent, null);
            }
            
        });
        
    }
    
    createReglement(evt, self) {
        
        var parent = dom.get("#prepend-body");
        self.renderOtherComponent("PopupReglement", { "action" : "create", "uid" : "", "title" : "", "content" : "" }, parent, null);
    }
    
    addWidget(evt, self) {
        var type = this.data("type");
        var parent = dom.get("#prepend-body");
        
        if ( type === "stream" ) {
            self.renderOtherComponent("PopupStream", {  }, parent, null);
        }
        
        if ( type === "candidat" ) {
            self.renderOtherComponent("PopupCandidat", {  }, parent, null);
        }
    }
    
    changeStateSwitch(evt, self) {
        var type = this.data("type");
        var uid = this.data("uid");
        var element = this;
        
        var url = "/api/site/active-widget/"+type+"/"+uid+"/";
        self.http.url = url;
        self.http.fetch(function(response) {
            
           if ( response.status === "success" ) {
               if ( response.active === true ) {
                   
                   var switch_active = dom.getAll(".widget-switch[data-type='"+type+"']");
                   if (switch_active.length > 0 ) {
                       switch_active.removeClass("active");
                   }
                   
                   element.addClass("active");
               }
               else {
                   element.removeClass("active");
               }
           } 
        });
    }
    
    afterRender() {
        
        var tabs = this.parent.find("#tabs-container-administrator");
        if (tabs !== null) {
            var tabs_plugin = tabs.runPlugin("tabs", { name_space : "administrator", current_language : "fr" });
        }
    }
    
    
}



class PopupStream extends Component {
    
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
                        var url = "/api/site/save-stream/";
                        self.http.url = url;
                        self.http.post(serialize, function(response) {
                           if ( response.status === "success" ) {
                               location.reload();
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
                    <h2 class="bottom30">Créer un  nouveau Stream</h2>
                    <form id="form-stream">
                        <p>
                            <label>Titre du Stream <span class="asterix">*</span></label>
                            <input type="text" name="title" placeholder="Example : Stream page home" class="required" data-rule="string" />
                        </p>
                        <p>
                            <label>Description du Stream</label>
                            <textarea name="description" data-rule="string" placeholder="Example : lorem ipsum"></textarea>
                        </p>

                        <p>
                            <label>Code du Stream <span class="asterix">*</span></label>
                            <textarea name="code" data-rule="string" class="required" placeholder="Example : lorem ipsum"></textarea>
                        </p>
                        
                        <p>
                            <span class="asterix">*</span> <span> : Champs obligatoires</span>
                        </p>

                        <div class="align-center top30">
                            <input type="button" value="Annuler" class="action-popup btn gris" data-action="close" />
                            <input type="button" value="Enregistrer" class="action-popup btn bleu" data-action="save" />
                        </div>
                        
                    </form>
                
                </div>
            </div>
      `; 
    }
}


class PopupCandidat extends Component {
    
    constructor(params) {
        super(params);
        
        this.events = {
            "click .action-popup" : "actionPopup"
            
        }
    }
    
    afterRender() {
        dom.get(".overlay-popup").animate(0.5, { "opacity" : 1});
        
        this.applyInputFiles();
    }
    
    
     applyInputFiles() {
        var self = this;
        var files = dom.getAll(".input-file-standard");
        var l_files = files.length;
        for (var f = 0; f < l_files; f++) {
            var input = files[f];
            self.utils.convertBase64(input, function(base64, file) {
                if (base64 !== "" && base64 !== null) {
                    var parent_children = this.getParent().find(".parent-children");
                    var input_base64 = this.getParent().find(".input-base64");
                    console.log(input_base64);
                    console.log(parent_children);
                    if ( input_base64 !== null ) {
                        input_base64.val(base64);
                    }
                    
                    if ( parent_children !== null ) {
                        parent_children.html("<img src='"+base64+"' class='full-width' />");
                    }
                    
                    
                }
                    
                    
             });
        }
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
                        var url = "/api/site/save-candidat/";
                        self.http.url = url;
                        self.http.post(serialize, function(response) {
                           if ( response.status === "success" ) {
                               location.reload();
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
                    <h2 class="bottom30">Créer un  nouveau Candidat</h2>
                    <form id="form-stream">
                        <h3 class="bottom30">Informations du Projet</h3>
                        <p>
                            <label>Titre du projet <span class="asterix">*</span></label>
                            <input type="text" name="title_project" placeholder="Example : Stream page home" class="required" data-rule="string" />
                        </p>
                        <p>
                            <label>Second Titre du projet <span class="asterix">*</span></label>
                            <input type="text" name="second_title_project" placeholder="Example : Stream page home" class="required" data-rule="string" />
                        </p>
                        <p>
                            <label>Contenu du projet</label>
                            <textarea name="content_project" data-rule="string" placeholder="Example : lorem ipsum"></textarea>
                        </p>

                        <p>
                            <label>Vidéo du projet  <span class="asterix">*</span></label>
                            <textarea name="video_project" class="required" data-rule="string" placeholder="Example : lorem ipsum"></textarea>
                        </p>

                        <h3 class="bottom30">Informations du Candidat</h3>

                        <p>
                            <label>Nom du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="first_name" data-rule="string" class="required" placeholder="Example : mohamed" />
                        </p>

                        <p>
                            <label>Prénom du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="last_name" data-rule="string" class="required" placeholder="Example : mohamed" />
                        </p>

                        <p>
                            <label>Email du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="email" data-rule="email" class="required" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>Site web du Candidat</label>
                            <input type="text" name="site_web" data-rule="string" class="" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>Lien Facebook du Candidat</label>
                            <input type="text" name="facebook" data-rule="string" class="" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>Lien Twitter du Candidat </label>
                            <input type="text" name="twitter" data-rule="string" class="" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>Position du Candidat </label>
                            <input type="text" name="position" data-rule="string" class="" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>Entreprise du Candidat </label>
                            <input type="text" name="company" data-rule="string" class="" placeholder="Example : example@example.com" />
                        </p>

                        <p>
                            <label>A propos du Candidat </label>
                            <textarea type="text" name="about" data-rule="string" class="" placeholder="Example : example@example.com" ></textarea>
                        </p>

                        <div id="container-upload" class="relative bottom20 top20">
                            <label>Photo du Candidat <span class="asterix">*</span></label>
                           <div id="upload-space" class="relative box-drag-drop file-input">
                               <input type="file" class="input-file-standard" name="photo" accept=".jpg, .jpeg, .png, .gif" />
                               <input type="hidden" class="required input-base64" data-rule="string" name="photo_base64" />
                                <div class="message-error-metric errors-message box26 align-center none"><h2></h2></div>
                                <div class="align-center drag-background">
                                    Cliquez pour Uploader la photo <br />
                                    Formats supportés : *JPG, *PNG, *GIF, *WEBM, MP4, MP3, OGG, WEBP

                                </div>
                                <div id="" class="row relative parent-children align-center">
                                    <div class="clr"></div>
                                </div>
                            </div>
                        </div>


                        <div class="align-center top30">
                            <input type="button" value="Annuler" class="action-popup btn gris" data-action="close" />
                            <input type="button" value="Enregistrer" class="action-popup btn bleu" data-action="save" />
                        </div>
                        
                    </form>
                
                </div>
            </div>
      `; 
    }
}


class PopupReglement extends Component {
    
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
                        var url = "/api/site/save-reglement/";
                        if ( self.props.action === "update" ) {
                            url = "/api/site/update-reglement/"+self.props.uid+"/";
                        }
                        self.http.url = url;
                        self.http.post(serialize, function(response) {
                           if ( response.status === "success" ) {
                               location.reload();
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
        console.log(this.props);
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Créer Régelement</h2>
                    <form id="form-stream">
                        <p class="none">
                            <input type="hidden" name="action" value="{{props.action}}" />
                            <input type="hidden" name="uid" value="{{props.uid}}" />
                        </p>
                        <p>
                        
                            <label>Titre du réglement <span class="asterix">*</span></label>
                            <input type="text" name="title" placeholder="Example : Réglement TOMBOLA" class="required" data-rule="string" value="{{props.title}}" />
                        </p>
                        <p>
                            <label>Contenu du réglement</label>
                            <textarea name="content" data-rule="string" placeholder="Example : lorem ipsum">{{props.content}}</textarea>
                        </p>

                        
                        
                        <p>
                            <span class="asterix">*</span> <span> : Champs obligatoires</span>
                        </p>

                        <div class="align-center top30">
                            <input type="button" value="Annuler" class="action-popup btn gris" data-action="close" />
                            <input type="button" value="Enregistrer" class="action-popup btn bleu" data-action="save" />
                        </div>
                        
                    </form>
                
                </div>
            </div>
      `; 
    }
}



invock.export("PopupReglement", PopupReglement);
invock.export("PopupStream", PopupStream);
invock.export("PopupCandidat", PopupCandidat);



invock.export("InterfaceAdministrator", InterfaceAdministrator);
invock.mount({ parent : "body", root : "{% InterfaceAdministrator parent_name='body' %}" });