dom.addPlugin("tabs", function(params) {
	var element = this;
	var parent = this.getParent();
	params = params || {};
    var name_space = params.name_space || "";
    var slider_tabs = dom.get(".slider-tabs-"+name_space);
    var width_tab = params.pas || dom.get(".container-tabs-"+name_space).width();
    var index_tab = 0;
    slider_tabs.findAll(".tab-"+name_space).css({ "width" : width_tab+"px" });
    var length_tabs = slider_tabs.findAll(".tab-"+name_space).length;
    
    var width_slider = (length_tabs*width_tab)+100;
    slider_tabs.css({ "width" : width_slider+"px" });
    if (element.findAll("li").length > 0) {
        element.findAll("li").eq(0).addClass("active");
    }
	element.findAll("ul.parent-ul > li:not(.no-tab)").on("click", function(evt) {
        var class_no_tab = this.hasClass("no-tab");
        if (!class_no_tab) {
            var index = this.index("li");
            index_tab = index;
            element.find("li.active").removeClass("active");
            this.addClass("active");
            slider_tabs.animate(0.5, { left : - (width_tab*index), ease : "easeOutExpo" });
            if (typeof params.callback === "function") {
                params.callback.call(this, index, slider_tabs);
            }
        }
        
		evt.preventDefault();
	}, true);
}); 