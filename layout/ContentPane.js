define([
	"dojo/_base/declare",
	"dojo/dom-construct",
	"dijit/layout/ContentPane",
	"dojo/dom-construct",
	"dojo/dom-style"
], function( declare, domConstruct, dContentPane, domConstruct, domStyle){

	// module:
	// mijit/layout/ContentPane
	
	var ContentPaneParentContainer = declare("dijit.layout._ContentPaneParentContainer", [], {
		
	});
	
	var ContentPane = declare("mijit.layout.ContentPane", dContentPane, {
		
		//A reference to wrapping div of ContentPane
		parentDomNode: null,
		
		width: null,
		
		height: null,
		
		_getwidhtValue: function(){
			return this.height;
		},
		
		_setwidhtValue: function(h){
			this.height = h;
		},
		
		buildRendering: function(){
			this.inherited(arguments);
		},
		
		postCreate: function(){
			// create the DOM for wrapping div of this widget
			this.parentDomNode = domConstruct.create("div");
			domConstruct.place(this.parentDomNode,this.domNode,"before");
			domConstruct.place(this.domNode,this.parentDomNode,"only");
			
			//rotate domNode
			domStyle.set(this.domNode,{
				"box-sizing":"border-box",
				//"transform-origin":"left top",
				//"transform":"rotate(-90deg) rotateY(180deg)",
			});			
			
			//reset width and height
			//var pcs = domStyle.getComputedStyle(this.parentDomNode);
			domStyle.set(this.domNode,{
				"width":"100%",
				"height":"100%"
			});
			
			var cs = domStyle.getComputedStyle(this.domNode);
			domStyle.set(this.parentDomNode,{
				//"width":cs.height,
				//"width":"fit-content"
				//"height":cs.width
			});
		}
	});

	return ContentPane;
});