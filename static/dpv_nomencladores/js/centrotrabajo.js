'use strict';

function abrir_modal(url, id=null)
{
    $('#popup').load(url, function()
    {
        $(this).modal('show');
    });

    return false;
}

function cerrar_modal()
{
    $('#popup').modal('hide');
    return false;
}

var DPVUnidadNom =  function () {
    let unidad_form;
    let validator_form;

    const _initUnidadPane = function (translations) {
        $('#unidad-table').DataTable({
            responsive: true,
            order: [ 0, 'desc' ],
            lengthMenu: [20, 35, 50, "All"],
            sScrollX: "100%",
            language: {
                "decimal": "",
                "emptyTable": translations.emptyTable,
                "info": translations.info_init + " _START_ a _END_ de _TOTAL_ " + translations.info_end,
                "infoEmpty": translations.infoEmpty,
                "infoFiltered": "(" + translations.infoFiltered_init + " _MAX_ " + translations.infoFiltered_end + ")",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": translations.lengthMenu_init + " _MENU_ " + translations.lengthMenu_end,
                "loadingRecords": translations.loadingRecords,
                "processing": translations.processing,
                "search":  translations.search,
                "zeroRecords": translations.zeroRecords,
                "paginate": {
                        "first": translations.first,
                        "last": translations.last,
                        "next": translations.next,
                        "previous": translations.previous,
                }
            },
        });
    };
    const _initUnidadForm =  function () {
        let $pj_prov = $("#id_municipio").selectize({
            create: false,
            placeholder: "Selecione un Municipio",
            allowEmptyOption: false,
        });

        const _fill_selectizes_with_values = function () {
            if ($("#id_municipio").val())
                $pj_prov[0].selectize.setValue($("#id_municipio").val());
        };

        $.validator.setDefaults({
            errorClass: 'text-danger',
            highlight: function(element) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function(element) {
                $(element).removeClass('is-invalid');
            },

			ignore: ":hidden",

            errorPlacement: function(error, element) {
                if (element[0].attributes['type'].nodeValue === 'select-one' || element[0].attributes['type'].nodeValue === 'select-multiple')
                    error.insertBefore(element.parent());
                else
                    error.insertBefore(element);
            },

        });
        $.validator.addMethod("letterswithbasicpuncandspace", function(value, element) {
            return this.optional(element) || /^[a-zA-Z0-9áéíóúÁÉÚÍÓñÑ \-.,()'"\s]+$/i.test(value);
        }, "solo puede tener letras, números, y signos de puntuación básicos");
        validator_form = unidad_form.validate({
			rules: {
				nombre: {
				    maxlength: 100,
				    required: true,
                    letterswithbasicpuncandspace: true,
                    remote: {
                        url: '/nomenclador/verify_unidad/',
                        type: 'GET',
                        data: {
                            id: unidad_id,
                        },
                    },
				},
				numero: {
				    maxlength: 3,
                    min: 1,
				    required: true,
                    digits: true,
                    remote: {
                        url: '/nomenclador/verify_unidad/',
                        type: 'GET',
                        data: {
                            id: unidad_id,
                        },
                    },
				},
				siglas: {
				    maxlength: 15,
				    required: true,
                    letterswithbasicpuncandspace: true,
				},
				municipio: {
				    required: true,
				},
			},
			messages: {
				nombre: {
				    maxlength: "El nombre de la unidad no puede tener más de 100 caracteres.",
				    required: "El nombre de la unidad es obligatorio.",
                    letterswithbasicpuncandspace: "El nombre de la unidad solo puede tener letras, números, y signos de puntuación básicos.",
                    remote: "Ya existe otra unidad registrada con ese nombre.",
				},
				numero: {
				    maxlength: "El número de la unidad no puede tener más de 3 dígitos.",
                    min: "El número de la unidad no puede ser menor que 1.",
				    required: "El número de la unidad es obligatorio.",
                    digits: "El número de la unidad solo puede tener dígitos.",
                    remote: "Ya existe otra unidad registrada con ese número.",
				},
				siglas: {
				    maxlength: "Las siglas de la unidad no puede tener más de 15 caracteres.",
				    required: "Las siglas de la unidad no puede quedar en blanco.",
                    letterswithbasicpuncandspace: "Las siglas de la unidad solo puede tener letras, números, y signos de puntuación básicos.",
				},
				municipio: {
				    required: "Tiene que seleccionar una municipio.",
				},
			},
		});
        _fill_selectizes_with_values();
    };

    return {
        init: function (translations) {
            _initUnidadPane(translations);
        },
        initForm: function () {
            unidad_form = $('#form_centtrab');
            _initUnidadForm();
        },
    }
}();