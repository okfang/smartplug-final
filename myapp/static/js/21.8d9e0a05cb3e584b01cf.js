webpackJsonp([21],{737:function(e,a,i){i(939);var t=i(1)(i(864),i(967),null,null);e.exports=t.exports},814:function(e,a,i){"use strict";a.a=["Afghanistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herzegowina","Botswana","Bouvet Island","Brazil","British Indian Ocean Territory","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central African Republic","Chad","Chile","China","Christmas Island","Cocos (Keeling) Islands","Colombia","Comoros","Congo","Congo, the Democratic Republic of the","Cook Islands","Costa Rica","Cote d'Ivoire","Croatia (Hrvatska)","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands (Malvinas)","Faroe Islands","Fiji","Finland","France","France Metropolitan","French Guiana","French Polynesia","French Southern Territories","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Heard and Mc Donald Islands","Holy See (Vatican City State)","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran (Islamic Republic of)","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, Democratic People's Republic of","Korea, Republic of","Kuwait","Kyrgyzstan","Lao, People's Democratic Republic","Latvia","Lebanon","Lesotho","Liberia","Libyan Arab Jamahiriya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia, The Former Yugoslav Republic of","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Micronesia, Federated States of","Moldova, Republic of","Monaco","Mongolia","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","Northern Mariana Islands","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russian Federation","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Seychelles","Sierra Leone","Singapore","Slovakia (Slovak Republic)","Slovenia","Solomon Islands","Somalia","South Africa","South Georgia and the South Sandwich Islands","Spain","Sri Lanka","St. Helena","St. Pierre and Miquelon","Sudan","Suriname","Svalbard and Jan Mayen Islands","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Taiwan, Province of China","Tajikistan","Tanzania, United Republic of","Thailand","Togo","Tokelau","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","United States Minor Outlying Islands","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Virgin Islands (British)","Virgin Islands (U.S.)","Wallis and Futuna Islands","Western Sahara","Yemen","Yugoslavia","Zambia","Zimbabwe"]},864:function(e,a,i){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var t=i(88),s=i.n(t),r=i(814),n=i(86),o=i.n(n);a.default={name:"form-wizard",components:{VuesticWizard:s.a,VuesticSimpleSelect:o.a},data:function(){var e=this;return{hsSteps:[{label:"Step 1. Name",slot:"page1",onNext:function(){e.validateFormField("hsName")},isValid:function(){return e.isFormFieldValid("hsName")}},{label:"Step 2. Country",slot:"page2",onNext:function(){e.$refs.hsCountrySelect.validate()},isValid:function(){return e.$refs.hsCountrySelect.isValid()}},{label:"Step 3. Confirm",slot:"page3"}],hrSteps:[{label:"Step 1. Name",slot:"page1",onNext:function(){e.validateFormField("hrName")},isValid:function(){return e.isFormFieldValid("hrName")}},{label:"Step 2. Country",slot:"page2",onNext:function(){e.$refs.hrCountrySelect.validate()},isValid:function(){return e.$refs.hrCountrySelect.isValid()}},{label:"Step 3. Confirm",slot:"page3"}],vrSteps:[{label:"Step 1. Name",slot:"page1",onNext:function(){e.validateFormField("vrName")},isValid:function(){return e.isFormFieldValid("vrName")}},{label:"Step 2. Country",slot:"page2",onNext:function(){e.$refs.vrCountrySelect.validate()},isValid:function(){return e.$refs.vrCountrySelect.isValid()}},{label:"Step 3. Confirm",slot:"page3"}],vsSteps:[{label:"Step 1. Name",slot:"page1",onNext:function(){e.validateFormField("vsName")},isValid:function(){return e.isFormFieldValid("vsName")}},{label:"Step 2. Country",slot:"page2",onNext:function(){e.$refs.vsCountrySelect.validate()},isValid:function(){return e.$refs.vsCountrySelect.isValid()}},{label:"Step 3. Confirm",slot:"page3"}],hsName:"",hsCountry:"",hrName:"",hrCountry:"",vrName:"",vrCountry:"",vsName:"",vsCountry:"",email:"",countriesList:r.a,chosenCountry:""}},methods:{isFormFieldValid:function(e){var a=!1;return this.fields[e]&&(a=this.fields[e].validated&&this.fields[e].valid),a},validateFormField:function(e){this.$validator.validate(e,this[e])}}}},911:function(e,a,i){a=e.exports=i(709)(),a.push([e.i,"\n.widget.simple-vertical-wizard-widget .widget-body {\n  padding: 0 1.5625rem;\n}\n@media (max-width: 767px) {\n.widget.simple-vertical-wizard-widget .widget-body {\n      padding: 1.5625rem 0;\n}\n}\n.form-wizard-page .form-group {\n  min-width: 200px;\n  max-width: 360px;\n  width: 80%;\n}\n","",{version:3,sources:["/Users/ycx/Desktop/swedenhack/vuestic-admin-master/src/components/forms/form-wizard/FormWizard.vue"],names:[],mappings:";AACA;EACE,qBAAqB;CACtB;AACD;AACA;MACM,qBAAqB;CAC1B;CACA;AACD;EACE,iBAAiB;EACjB,iBAAiB;EACjB,WAAW;CACZ",file:"FormWizard.vue",sourcesContent:["\n.widget.simple-vertical-wizard-widget .widget-body {\n  padding: 0 1.5625rem;\n}\n@media (max-width: 767px) {\n.widget.simple-vertical-wizard-widget .widget-body {\n      padding: 1.5625rem 0;\n}\n}\n.form-wizard-page .form-group {\n  min-width: 200px;\n  max-width: 360px;\n  width: 80%;\n}\n"],sourceRoot:""}])},939:function(e,a,i){var t=i(911);"string"==typeof t&&(t=[[e.i,t,""]]),t.locals&&(e.exports=t.locals);i(710)("646b0152",t,!0)},967:function(e,a){e.exports={render:function(){var e=this,a=e.$createElement,i=e._self._c||a;return i("div",{staticClass:"form-wizard-page"},[i("div",{staticClass:"row"},[i("div",{staticClass:"col-md-12"},[i("vuestic-widget",{staticClass:"no-h-padding",attrs:{headerText:"Simple Wizard"}},[i("vuestic-wizard",{attrs:{steps:e.hsSteps}},[i("div",{staticClass:"form-wizard-tab-content",slot:"page1"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("div",{staticClass:"form-group with-icon-right",class:{"has-error":e.errors.has("hsName"),valid:e.isFormFieldValid("hsName")}},[i("div",{staticClass:"input-group"},[i("input",{directives:[{name:"model",rawName:"v-model",value:e.hsName,expression:"hsName"},{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"hsName",required:"",title:""},domProps:{value:e.hsName},on:{input:function(a){a.target.composing||(e.hsName=a.target.value)}}}),e._v(" "),i("i",{staticClass:"fa fa-exclamation-triangle error-icon icon-right input-icon"}),e._v(" "),i("i",{staticClass:"fa fa-check valid-icon icon-right input-icon"}),e._v(" "),i("label",{staticClass:"control-label"},[e._v("Name")]),i("i",{staticClass:"bar"}),e._v(" "),i("small",{directives:[{name:"show",rawName:"v-show",value:e.errors.has("hsName"),expression:"errors.has('hsName')"}],staticClass:"help text-danger"},[e._v(e._s(e.errors.first("hsName")))])])])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page2"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("vuestic-simple-select",{ref:"hsCountrySelect",attrs:{label:"Select country",name:"country",required:!0,options:e.countriesList},model:{value:e.hsCountry,callback:function(a){e.hsCountry=a},expression:"hsCountry"}})],1),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page3"},[i("h4",[e._v("Confirm selection")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"wizardCompleted"},[i("h4",[e._v("Wizard completed!")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])])])],1)],1)]),e._v(" "),i("div",{staticClass:"row"},[i("div",{staticClass:"col-md-12"},[i("vuestic-widget",{staticClass:"no-h-padding",attrs:{headerText:"Rich Wizard"}},[i("vuestic-wizard",{attrs:{steps:e.hrSteps,"wizard-type":"rich"}},[i("div",{staticClass:"form-wizard-tab-content",slot:"page1"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("div",{staticClass:"form-group with-icon-right",class:{"has-error":e.errors.has("hrName"),valid:e.isFormFieldValid("hrName")}},[i("div",{staticClass:"input-group"},[i("input",{directives:[{name:"model",rawName:"v-model",value:e.hrName,expression:"hrName"},{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"hrName",required:"",title:""},domProps:{value:e.hrName},on:{input:function(a){a.target.composing||(e.hrName=a.target.value)}}}),e._v(" "),i("i",{staticClass:"fa fa-exclamation-triangle error-icon icon-right input-icon"}),e._v(" "),i("i",{staticClass:"fa fa-check valid-icon icon-right input-icon"}),e._v(" "),i("label",{staticClass:"control-label"},[e._v("Name")]),i("i",{staticClass:"bar"}),e._v(" "),i("small",{directives:[{name:"show",rawName:"v-show",value:e.errors.has("hrName"),expression:"errors.has('hrName')"}],staticClass:"help text-danger"},[e._v(e._s(e.errors.first("hrName")))])])])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page2"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("vuestic-simple-select",{ref:"hrCountrySelect",attrs:{label:"Select country",name:"country",required:!0,options:e.countriesList},model:{value:e.hrCountry,callback:function(a){e.hrCountry=a},expression:"hrCountry"}})],1),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page3"},[i("h4",[e._v("Confirm selection")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"wizardCompleted"},[i("h4",[e._v("Wizard completed!")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])])])],1)],1)]),e._v(" "),i("div",{staticClass:"row"},[i("div",{staticClass:"col-md-12"},[i("vuestic-widget",{attrs:{headerText:"Vertical Rich Wizard"}},[i("vuestic-wizard",{attrs:{steps:e.vrSteps,"wizard-layout":"vertical","wizard-type":"rich"}},[i("div",{staticClass:"form-wizard-tab-content",slot:"page1"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("div",{staticClass:"form-group with-icon-right",class:{"has-error":e.errors.has("vrName"),valid:e.isFormFieldValid("vrName")}},[i("div",{staticClass:"input-group"},[i("input",{directives:[{name:"model",rawName:"v-model",value:e.vrName,expression:"vrName"},{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"vrName",required:"",title:""},domProps:{value:e.vrName},on:{input:function(a){a.target.composing||(e.vrName=a.target.value)}}}),e._v(" "),i("i",{staticClass:"fa fa-exclamation-triangle error-icon icon-right input-icon"}),e._v(" "),i("i",{staticClass:"fa fa-check valid-icon icon-right input-icon"}),e._v(" "),i("label",{staticClass:"control-label"},[e._v("Name")]),i("i",{staticClass:"bar"}),e._v(" "),i("small",{directives:[{name:"show",rawName:"v-show",value:e.errors.has("vrName"),expression:"errors.has('vrName')"}],staticClass:"help text-danger"},[e._v(e._s(e.errors.first("vrName")))])])])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page2"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("vuestic-simple-select",{ref:"vrCountrySelect",attrs:{label:"Select country",name:"country",required:!0,options:e.countriesList},model:{value:e.vrCountry,callback:function(a){e.vrCountry=a},expression:"vrCountry"}})],1),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page3"},[i("h4",[e._v("Confirm selection")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"wizardCompleted"},[i("h4",[e._v("Wizard completed!")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])])])],1)],1)]),e._v(" "),i("div",{staticClass:"row"},[i("div",{staticClass:"col-md-12"},[i("vuestic-widget",{staticClass:"simple-vertical-wizard-widget",attrs:{headerText:"Vertical Simple Wizard"}},[i("vuestic-wizard",{attrs:{steps:e.vsSteps,"wizard-layout":"vertical","wizard-type":"simple"}},[i("div",{staticClass:"form-wizard-tab-content",slot:"page1"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("div",{staticClass:"form-group with-icon-right",class:{"has-error":e.errors.has("vsName"),valid:e.isFormFieldValid("vsName")}},[i("div",{staticClass:"input-group"},[i("input",{directives:[{name:"model",rawName:"v-model",value:e.vsName,expression:"vsName"},{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],attrs:{name:"vsName",required:"",title:""},domProps:{value:e.vsName},on:{input:function(a){a.target.composing||(e.vsName=a.target.value)}}}),e._v(" "),i("i",{staticClass:"fa fa-exclamation-triangle error-icon icon-right input-icon"}),e._v(" "),i("i",{staticClass:"fa fa-check valid-icon icon-right input-icon"}),e._v(" "),i("label",{staticClass:"control-label"},[e._v("Name")]),i("i",{staticClass:"bar"}),e._v(" "),i("small",{directives:[{name:"show",rawName:"v-show",value:e.errors.has("vsName"),expression:"errors.has('vsName')"}],staticClass:"help text-danger"},[e._v(e._s(e.errors.first("vsName")))])])])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page2"},[i("p",[e._v('Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"')]),e._v(" "),i("vuestic-simple-select",{ref:"vsCountrySelect",attrs:{label:"Select country",name:"country",required:!0,options:e.countriesList},model:{value:e.vsCountry,callback:function(a){e.vsCountry=a},expression:"vsCountry"}})],1),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"page3"},[i("h4",[e._v("Confirm selection")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])]),e._v(" "),i("div",{staticClass:"form-wizard-tab-content",slot:"wizardCompleted"},[i("h4",[e._v("Wizard completed!")]),e._v(" "),i("p",[e._v('\n              Zebras communicate with facial expressions and sounds. They make loud braying or barking sounds and\n              soft snorting sounds. The position of their ears, how wide open their eyes are, and whether they show\n              their teeth all send a signal. For example, ears flat back means trouble, or "you better follow orders!"\n            ')])])])],1)],1)])])},staticRenderFns:[]}}});
//# sourceMappingURL=21.8d9e0a05cb3e584b01cf.js.map