define([
	"dojo/_base/declare",
	"dojo/dom-construct",
	"dijit/layout/ContentPane"
], function( declare, domConstruct, dContentPane ){

	// module:
	// mijit/layout/ContentPane

	return declare("mijit.layout.ContentPane", dContentPane, {
		buildRendering: function(){
			this.inherited(arguments);
		},
		postCreate: function(){
			// create the DOM for this widget
			
		}
	});
});