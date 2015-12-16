define([
	"dojo/_base/declare",
	"dojo/dom-construct",
	"dijit/layout/ContentPane",
	"dojo/dom-construct",
	"dojo/dom-style"
], function( declare, domConstruct, dContentPane, domConstruct, domStyle){

	// module:
	// mijit/layout/ContentPane

	return declare("mijit.layout.ContentPane", dContentPane, {
		
		//A reference to wrapping div of ContentPane
		parentDomNode: null,
		
		buildRendering: function(){
			this.inherited(arguments);
		},
		
		postCreate: function(){
			// create the DOM for wrapping div of this widget
			this.parentDomNode = domConstruct.create("div");
			domConstruct.place(this.parentDomNode,this.domNode,"before");
			domConstruct.place(this.domNode,this.parentDomNode,"only");
			
			//rotate domNode
			//domStyle.set(this.domNode,"transform-origin","left top");
			domStyle.set(this.domNode,"transform","rotateZ(-90deg)");
			domStyle.set(this.domNode,"transform","rotate(180deg)");
			
		}
	});
});