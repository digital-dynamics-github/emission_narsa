import invock, {Component} from "invock-js";
import Plugins from "../plugins/plugins";

class InterfaceAdministrator extends Component {
    constructor(params) {
        super(params);
        
        this.events = {
            "click .widget-switch" : "changeStateSwitch",
            "click .add-widget" : "addWidget",
            "click .update-widget" : "updateWidget",
            "click .delete-widget" : "deleteWidget",
            "click #create-reglement" : "createReglement",
            "click #update-reglement" : "updateReglement",
        }
        
    }
    
    
    deleteWidget(evt, self) {
        var uid = this.data("uid");
        var element = this.data("type");
        var url = "/api/site/delete-element/"+element+"/"+uid+"/";
        self.http.url = url;
        self.http.fetch(function (response) {
           if ( response.status === "success" ) {
               location.reload();
           } 
        });
    }
    
    updateReglement(evt, self) {
        var uid = this.data("id");
        
        var url = "/api/site/get-reglement/"+uid+"/";
        self.http.url = url;
        self.http.fetch(function(response) {
            if ( response.data !== null ) {
                var parent = dom.get("#prepend-body");
                self.renderOtherComponent("PopupReglement", { "action" : "update", "uid" : uid, "title" : response.data.title, "content" : response.data.content, "title_ar" : response.data.title_ar," content_ar" : response.data.content_ar }, parent, null);
            }
            
        });
        
    }
    
    createReglement(evt, self) {
        
        var parent = dom.get("#prepend-body");
        self.renderOtherComponent("PopupReglement", { "action" : "create", "uid" : "", "title" : "", "content" : "" }, parent, null);
    }
    
    updateWidget(evt, self) {
        var type = this.data("type");
        var uid = this.data("uid");
        var parent = dom.get("#prepend-body");
        var props = {};
        
        
        
        if ( type === "stream" ) {
            
            self.http.url = "/api/site/get-stream/"+uid+"/";
            self.http.fetch(function(response) {
               
                props = response.data;
                props.uid = uid;
                props.action = "update";
                self.renderOtherComponent("PopupStream", props, parent, null);
                
            });
            
            
        }
        
        if ( type === "candidat" ) {
            self.http.url = "/api/site/get-candidat/"+uid+"/";
            self.http.fetch(function(response) {
               
                props = response.data;
                props.uid = uid;
                props.action = "update";
                self.renderOtherComponent("PopupCandidat", props, parent, null);
                
            });
        }
        
        if ( type === "jury" ) {
            
            self.http.url = "/api/site/get-jury/"+uid+"/";
            self.http.fetch(function(response) {
               
                props = response.data;
                props.uid = uid;
                props.action = "update";
                self.renderOtherComponent("PopupJury", props, parent, null);
                
            });
        }
        
        
        if ( type === "block_text" || type === "block_script") {
            
            self.http.url = "/api/site/get-block-text/"+uid+"/";
            self.http.fetch(function(response) {
               
                props = response.data;
                props.uid = uid;
                props.action = "update";
                self.renderOtherComponent("PopupBlockText", props, parent, null);
                
            });
        }
    }
    
    
    addWidget(evt, self) {
        var type = this.data("type");
        var parent = dom.get("#prepend-body");
        var props = {
            
        }
        
        if ( type === "stream" ) {
            
            props = {
                "action" : "create",
                "uid" : "",
                "title" : "",
                "description" : "",
                "title_ar" : "",
                "description_ar" : "",
                "code" : "",
                "code_ar" : "",
            }
            
            self.renderOtherComponent("PopupStream", props, parent, null);
        }
        
        if ( type === "candidat" ) {
            props = {
                "action" : "create",
                "uid" : "",
                "title_project" : "",
                "second_title_project" : "",
                "content_project" : "",
                "video_project" : "",
                
                "title_project_ar" : "",
                "content_project_ar" : "",
                "video_project_ar" : "",
                
                "first_name" : "",
                "last_name" : "",
                "email" : "",
                "site_web" : "",
                "facebook" : "",
                "twitter" : "",
                "about" : "",
                "position" : "",
                "company" : "",
                
                "first_name_ar" : "",
                "last_name_ar" : "",
                "about_ar" : "",
                "position_ar" : "",
                "company_ar" : "",
                "category_project" : "",
                "category_project_ar" : "",
            }
            self.renderOtherComponent("PopupCandidat", props, parent, null);
        }
        
        if ( type === "jury" ) {
            props = {
                "action" : "create",
                "uid" : "",
                "first_name" : "",
                "last_name" : "",
                "email" : "",
                "site_web" : "",
                "facebook" : "",
                "twitter" : "",
                "about" : "",
                "position" : "",
                "company" : "",
                
                "first_name_ar" : "",
                "last_name_ar" : "",
                "about_ar" : "",
                "position_ar" : "",
                "company_ar" : "",
            }
            self.renderOtherComponent("PopupJury", props, parent, null);
        }
        
        if ( type === "block_text" || type === "block_script") {
            var location_block = "home";
            
            if (type === "block_script") {
                location_block = "script"
            }
            props = {
                "action" : "create",
                "uid" : "",
                "title" : "",
                "description" : "",
                "title_ar" : "",
                "description_ar" : "",
                "location" : location_block
                
            }
            
            self.renderOtherComponent("PopupBlockText", props, parent, null);
        }
        
    }
    
    changeStateSwitch(evt, self) {
        var type = this.data("type");
        var uid = this.data("uid");
        var element = this;
        var label_switcher = this.find(".label-switcher");
        
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
                   if( label_switcher !== null ) {
                       label_switcher.html("Active");
                   }
               }
               else {
                   element.removeClass("active");
                   if( label_switcher !== null ) {
                       label_switcher.html("Non Active");
                   }
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
                        if ( self.props.action === "update" ) {
                            url = "/api/site/update-stream/"+self.props.uid+"/";
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
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Stream</h2>
                    <form id="form-stream">
                        <p class="none">
                            <label>Titre du Stream <span class="asterix">*</span></label>
                            <input type="text" name="title" placeholder="Example : Stream page home" class="" data-rule="string" value="{{props.title}}" />
                        </p>
                        <p class="none">
                            <label>Description du Stream</label>
                            <textarea name="description" data-rule="string" placeholder="Example : lorem ipsum">{{props.description}}</textarea>
                        </p>
                        <p class="none">
                            <label>Titre du Stream <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="title_ar" placeholder="Example : Stream page home" class="" data-rule="string" value="{{props.title_ar}}" />
                        </p>
                        <p class="none">
                            <label>Description du Stream <span class="bold">en ARABE</span></label>
                            <textarea name="description_ar" data-rule="string" placeholder="Example : lorem ipsum">{{props.description_ar}}</textarea>
                        </p>

                        <p>
                            <label>Code du Stream <span class="asterix">*</span></label>
                            <textarea name="code" data-rule="string" class="required" placeholder="Example : lorem ipsum">{{props.code}}</textarea>
                        </p>

                        <p>
                            <label>Code <span class="bold">ARABE</span> du Stream <span class="asterix">*</span></label>
                            <textarea name="code_ar" data-rule="string" class="required" placeholder="Example : lorem ipsum">{{props.code_ar}}</textarea>
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
                        if ( self.props.action === "update" ) {
                            url = "/api/site/update-candidat/"+self.props.uid+"/";
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
                    <h2 class="bottom30">Candidat</h2>
                    <form id="form-stream">
                        <h3 class="bottom30">Informations du Projet</h3>
                        <p>
                            <label>Titre du projet <span class="asterix">*</span></label>
                            <input type="text" name="title_project" placeholder="Example : Stream page home" class="required" data-rule="string" value="{{props.title_project}}" />
                        </p>
                        <p class="">
                            <label>Catégorie du projet </label>
                            <input type="text" name="category_project" placeholder="Example : Stream page home" class="" data-rule="string" value="{{props.category_project}}" />
                        </p>
                       
                        <p>
                            <label>Contenu du projet  <span class="asterix">*</span></label>
                            <textarea name="content_project" class="required" data-rule="string" placeholder="Example : lorem ipsum">{{props.content_project}}</textarea>
                        </p>
                        <p>
                            <label>Titre du projet  <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="title_project_ar" placeholder="Example : Stream page home" class="required" data-rule="string" value="{{props.title_project_ar}}" />
                        </p>
                         
                        <p>
                            <label>Contenu du projet  <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <textarea name="content_project_ar" class="required" data-rule="string" placeholder="Example : lorem ipsum">{{props.content_project_ar}}</textarea>
                        </p>

                        <p class="">
                            <label>Catégorie du projet <span class="bold">en ARABE</span></label>
                            <input type="text" name="category_project_ar" placeholder="Example : Stream page home" class="" data-rule="string" value="{{props.category_project_ar}}" />
                        </p>


                        <p>
                            <label>Vidéo du projet  <span class="asterix">*</span></label>
                            <textarea name="video_project" class="required" data-rule="string" placeholder="Example : lorem ipsum">{{props.video_project}}</textarea>
                        </p>

                        <h3 class="bottom30 top30">Informations du Candidat</h3>

                        <p>
                            <label>Nom du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="first_name" data-rule="string" class="required" placeholder="Example : mohamed" value="{{props.first_name}}" />
                        </p>

                        <p>
                            <label>Prénom du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="last_name" data-rule="string" class="required" placeholder="Example : mohamed" value="{{props.last_name}}" />
                        </p>
                         <p>
                            <label>Position du Candidat </label>
                            <input type="text" name="position" data-rule="string" class="" placeholder="Example : lorem ipsum" value="{{props.position}}" />
                        </p>

                         <p>
                            <label>Nom du Candidat <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="first_name_ar" data-rule="string" class="required" placeholder="Example : mohamed" value="{{props.first_name_ar}}" />
                        </p>

                        <p>
                            <label>Prénom du Candidat <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="last_name_ar" data-rule="string" class="required" placeholder="Example : mohamed" vale="{{props.last_name_ar}}" />
                        </p>

                       

                        <p>
                            <label>Position du Candidat <span class="bold">en ARABE</span></label>
                            <input type="text" name="position_ar" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.position_ar}}" />
                        </p>

                        
                        
                        <p class="none">
                            <label>Second Titre du projet <span class="asterix">*</span></label>
                            <input type="text" name="second_title_project" placeholder="Example : Stream page home" class="" data-rule="string" value="{{props.second_title_project}}" />
                        </p>
                        <p class="none">
                            <label>Second Titre du projet  <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="second_title_project_ar" placeholder="Example : Stream page home" class="required" data-rule="string" value="{{props.second_title_project_ar}}" />
                        </p>
                        <p class="none">
                            <label>Email du Candidat <span class="asterix">*</span></label>
                            <input type="text" name="email" data-rule="" class="" placeholder="Example : example@example.com" value="{{props.email}}" />
                        </p>

                        <p class="none">
                            <label>Site web du Candidat</label>
                            <input type="text" name="site_web" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.site_web}}" />
                        </p class="none">

                        <p class="none">
                            <label>Lien Facebook du Candidat</label>
                            <input type="text" name="facebook" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.facebook}}" />
                        </p>

                        <p class="none">
                            <label>Lien Twitter du Candidat </label>
                            <input type="text" name="twitter" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.twitter}}" />
                        </p>

                       
                        <p class="none">
                            <label>Entreprise du Candidat </label>
                            <input type="text" name="company" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.company}}" />
                        </p>

                        <p class="none">
                            <label>A propos du Candidat </label>
                            <textarea type="text" name="about" data-rule="string" class="" placeholder="Example : example@example.com" >{{props.about}}</textarea>
                        </p>

                        

                        <p class="none">
                            <label>Entreprise du Candidat <span class="bold">en ARABE</span></label>
                            <input type="text" name="company_ar" data-rule="string" class="" placeholder="Example : example@example.com" value="{{props.company_ar}}" />
                        </p>

                        <p class="none">
                            <label>A propos du Candidat <span class="bold">en ARABE</span> </label>
                            <textarea type="text" name="about_ar" data-rule="string" class="" placeholder="Example : example@example.com" >{{props.about_ar}}</textarea>
                        </p>

                        <div id="container-upload" class="relative bottom20 top20">
                            <label>Photo du Candidat <span class="asterix">*</span></label>
                           <div id="upload-space" class="relative box-drag-drop file-input">
                               <input type="file" class="input-file-standard" name="photo" accept=".jpg, .jpeg, .png, .gif" />
                               <input type="hidden" class="input-base64" data-rule="string" name="photo_base64" />
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
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Régelement</h2>
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
                        
                            <label>Titre du réglement <span class="bold">en ARABE</span><span class="asterix">*</span></label>
                            <input type="text" name="title_ar" placeholder="Example : Réglement TOMBOLA" class="required" data-rule="string" value="{{props.title_ar}}" />
                        </p>
                        <p>
                            <label>Contenu du réglement <span class="bold">en ARABE</span><span class="asterix">*</span></label>
                            <textarea name="content_ar" data-rule="string" placeholder="Example : lorem ipsum">{{props.content_ar}}</textarea>
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

class PopupBlockText extends Component {
    
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
                        var url = "/api/site/save-block-text/";
                        if ( self.props.action === "update" ) {
                            url = "/api/site/update-block-text/"+self.props.uid+"/";
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
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Block Text  / Block Script</h2>
                    <form id="form-stream">
                        <p class="none">
                            <input type="hidden" name="action" value="{{props.action}}" />
                            <input type="hidden" name="uid" value="{{props.uid}}" />
                            <input type="hidden" name="location" value="{{props.location}}" />
                        </p>
                        <p>
                        
                            <label>Titre <span class="asterix">*</span></label>
                            <input type="text" name="title" placeholder="Example : Réglement TOMBOLA" class="required" data-rule="string" value="{{props.title}}" />
                        </p>
                        <p>
                            <label>Contenu  <span class="asterix">*</span></label>
                            <textarea name="description" class="required" data-rule="string" placeholder="Example : lorem ipsum">{{props.description}}</textarea>
                        </p>

                        <p>
                        
                            <label>Titre  <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="title_ar" placeholder="Example : Réglement TOMBOLA" class="required" data-rule="string" value="{{props.title_ar}}" />
                        </p>
                        <p>
                            <label>Contenu  <span class="bold">en ARABE</span>  <span class="asterix">*</span></label>
                            <textarea name="description_ar" class="required" data-rule="string" placeholder="Example : lorem ipsum">{{props.description_ar}}</textarea>
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


class PopupJury extends Component {
    
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
                        var url = "/api/site/save-jury/";
                        if ( self.props.action === "update" ) {
                            url = "/api/site/update-jury/"+self.props.uid+"/";
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
    
    
    
    
    render() {
        return `
       
            <div class="overlay-popup"></div>
            <div class="container-popup">
                <div class="box-popup relative center-auto border shadow">
                    <h2 class="bottom30">Jury</h2>
                    <form id="form-stream">
                        <p>
                        
                            <label>Nom du Jury <span class="asterix">*</span></label>
                            <input type="text" name="first_name" placeholder="Example : benjawad" class="required" data-rule="string" value="{{props.first_name}}" />
                        </p>
                        <p>
                        
                            <label>prénom du Jury <span class="asterix">*</span></label>
                            <input type="text" name="last_name" placeholder="Example : ahmed" class="required" data-rule="string" value="{{props.last_name}}" />
                        </p>
                        
                        <p>
                        
                            <label>Nom du Jury <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="first_name_ar" placeholder="Example : benjawad" class="required" data-rule="string" value="{{props.first_name_ar}}" />
                        </p>
                        <p>
                        
                            <label>prénom du Jury <span class="bold">en ARABE</span> <span class="asterix">*</span></label>
                            <input type="text" name="last_name_ar" placeholder="Example : ahmed" class="required" data-rule="string" value="{{props.last_name_ar}}" />
                        </p>

                        <p class="none">
                        
                            <label>Adresse Email du Jury <span class="asterix">*</span></label>
                            <input type="text" name="email" placeholder="Example : ahmed" class="" data-rule="email" value="{{props.email}}" />
                        </p>
                        
                        <p class="">
                            <label>A propos du Jury</label>
                            <textarea name="about" data-rule="string" placeholder="Example : lorem ipsum">{{props.about}}</textarea>
                        </p>

                        <p class="">
                            <label>A propos du Jury  <span class="bold">en ARABE</span></label>
                            <textarea name="about_ar" data-rule="string" placeholder="Example : lorem ipsum">{{props.about_ar}}</textarea>
                        </p>

                        <p>
                            <label>Position du Jury</label>
                            <input type="text" name="position" placeholder="Example : ahmed" class="required" data-rule="string" value="{{props.position}}" />
                        </p>

                        <p>
                            <label>Position du Jury  <span class="bold">en ARABE</span></label>
                             <input type="text" name="position_ar" placeholder="Example : ahmed" class="required" data-rule="string" value="{{props.position_ar}}" />
                        </p>


                        <p class="">
                            <label>Catégorie du Jury</label>
                             <input type="text" name="company" placeholder="Example : ahmed" class="" data-rule="string" value="{{props.company}}" />
                        </p>

                        <p class="">
                            <label>Catégorie du Jury  <span class="bold">en ARABE</span></label>
                            <input type="text" name="company_ar" placeholder="Example : ahmed" class="" data-rule="string" value="{{props.company_ar}}" />
                        </p>
                        
                        
                        <p>
                        
                            <label>Site web du Jury</label>
                            <input type="text" name="site_web" placeholder="Example : http://example.com" class="" data-rule="string" value="{{props.site_web}}" />
                        </p>

                        <p>
                        
                            <label>Facebook du Jury</label>
                            <input type="text" name="facebook" placeholder="Example : http://example.com" class="" data-rule="string" value="{{props.facebook}}" />
                        </p>

                        <p>
                        
                            <label>Twitter du Jury </label>
                            <input type="text" name="twitter" placeholder="Example : http://example.com" class="" data-rule="string" value="{{props.twitter}}" />
                        </p>
                        
                        
                        


                         <div id="container-upload" class="relative bottom20 top20">
                            <label>Photo du Jury <span class="asterix">*</span></label>
                           <div id="upload-space" class="relative box-drag-drop file-input">
                               <input type="file" class="input-file-standard" name="photo" accept=".jpg, .jpeg, .png, .gif" />
                               <input type="hidden" class="input-base64" data-rule="string" name="photo_base64" />
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
invock.export("PopupBlockText", PopupBlockText);
invock.export("PopupStream", PopupStream);
invock.export("PopupCandidat", PopupCandidat);
invock.export("PopupJury", PopupJury);



invock.export("InterfaceAdministrator", InterfaceAdministrator);
invock.mount({ parent : "body", root : "{% InterfaceAdministrator parent_name='body' %}" });