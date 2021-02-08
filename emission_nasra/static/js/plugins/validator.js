import invock, {dom, utils} from "invock-js";

dom.addPlugin("validator", function(params) {
	var element = this;
	params = params || {};
    var parent_validator = params.parent || element.closests("form");
    
    params.createMessage = function(type, message) {
        if (typeof message !== "undefined" && message !== null) {
            return message;
        }
        else {
            
            message = "";
            switch(type) {
                case "string" : 
                    message = "This field is required";
                break;
                case "number" : 
                    message = "Enter valid number";
                break;
                case "phone" : 
                    message = "Enter valid phone number";
                break;
                case "email" : 
                    message = "Enter valid adress email";
                break;
                case "password" : 
                    message = "Your password must contain at least 8 characters";
                break;
                case "date" : 
                    message = "Enter valid date format YYYY/MM/DD or DD/MM/YYYY";
                break;
                case "string_code" : 
                    message = "Enter valid code";
                break;
            }
            return message;
        }
        
        
    };
    
    params.isRequired = function(input, message) {
        var value = input.val();
		if( (value.length > 0 && value !== null && typeof value !== "undefined") || input.checked === true) {
			return !this.addErrorInput(input, false);
		}
		else {
			return !this.addErrorInput(input, true, message);
		}
    };
    
    params.addErrorInput = function(input, apply, message) {
        
        if( apply ) {
			input.addClass("error");
            input.getParent().addClass("error-p");
            var type_input = input.attr("type");
            if (type_input !== "checkbox" && type_input !== "radio") {
                input.after('<span class="message-error-input"><span class="inline-block">'+message+'</span></span>');
            }
            else {
                input.getParent().appendTo('<span class="message-error-input"><span class="inline-block">'+message+'</span></span>');
            }
		}
		else {
			input.removeClass("error");
			input.addClass("done");
            input.getParent().removeClass("error-p");
            input.getParent().findAll(".message-error-input").remove();
		}
		return apply;
    };
    
    
    function verifyTextField(value) {
        if ( value.length > 200 ) {
            return false;
        }
        else {
            return true;
        }
    }
    
    var inupts = parent_validator.findAll(".required");
    var nbr_input = inupts.length;
		var test_passe = [];
		for( var i = 0; i < nbr_input; i++ ) {
			var input = parent_validator.findAll(".required").eq(i);
            
            
            
            var attr_name_input = input.attr("name");
            if (typeof attr_name_input !== "undefined" &&  attr_name_input !== null && attr_name_input !== "" ) {
                var rule = input.data("rule");
                var message = input.data("message");
                var value = input.val();
                var status_text = true;
                
                
                
                if (input.attr("type") === "checkbox" || input.attr("type") === "radio") {
                    value = input.checked;
                }
                input.removeClass("error");
                input.getParent().removeClass("error-p");
                input.getParent().findAll(".message-error-input").remove();
                if (message  === null) {
                    message = "This field is required";
                }
                if( params.isRequired(input, message) ) {
                    
                    if (input.attr("type") === "checkbox" || input.attr("type") === "radio") {
                        if (input.checked === true) {
                            params.addErrorInput(input, false, params.createMessage(rule, message));
                            test_passe.push(value);
                        }
                        else {
                            params.addErrorInput(input, true, params.createMessage(rule, message));
                            test_passe.pop();
                        }
                    }
                    
                    if( typeof rule !== "undefined" && rule !== null && rule !== "" ) {
                        
                        if ( input.attr("type") === "text" ) {
                            status_text = verifyTextField(value);
                        }
                        
                        
                        var rule_accept = utils["is_"+rule](value);
                        if(rule_accept && status_text === true && input.attr("type") !== "checkbox" && input.attr("type") !== "radio" ) {
                            params.addErrorInput(input, false, params.createMessage(rule, message));
                            
                            test_passe.push(value);
                        }
                        else {
                            
                            if ( input.attr("type") !== "checkbox" && input.attr("type") !== "radio"  ) {
                                if ( status_text === false ) {
                                    params.addErrorInput(input, true, params.createMessage(rule, "le nombre des caractéres autorisé il ne doit pas supérieur à 200 caractéres"));
                                    test_passe.pop();
                                }
                                else {
                                    params.addErrorInput(input, true, params.createMessage(rule, message));
                                    test_passe.pop();
                                }
                            }
                            
                            
                        }
                    }
                }
               
            } 
		}// for
    
		if( test_passe.length === nbr_input || inupts.length === 0 ) {
            if (typeof params.valid === "function" && params.valid !== null) {
                
                params.valid.call(this, true, "OK", nbr_input, test_passe.length);
            }
		}
        else {
            if (typeof params.error === "function" && params.error !== null) {
                params.error.call(this, false, "ERROR");
            }
        }
    
    
    
}); 