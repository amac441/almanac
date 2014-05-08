/***************ANGULARJS FUNCTION****************/
function langLoved($scope) {

    $scope.languages = [{
            text: 'AngularJS',
            desc: 'É MVC, a aplicação é escrita em componentes separados e o AngularJS depois atua como cola entre eles. Usa o HTML para declarar a UI (data-binding) e definir a execução da app. Permite diretivas para definir comportamentos como tabs, acordeão, grid: <tab></tab> <accordion></accordion>. Escrevemos muito menos HTML pelo facto de tornar o HTML em templates.'
        },

        {
            text: 'HTML5',
            desc: 'Power to HTML! Suporte para audio e video, maior índice de acessibilidade por termos uma nova semântica. HTML mais limpo, possibilidade de usar local storage para guardar dados localmente, funcionalidde de drag and drop, uso de canvas para gráficos... Uma outra grande vantagem de usar HTML5 é a sua integração com dispositivos móveis e a facilidade de o usar com bibliotecas como o phonegap para criar aplicações web para mobile.'
        },

        {
            text: 'CSS3',
            desc: 'A possibilidade de completar o processo de design no browser. Inovação em animações 2D e 3D, novos seletores, layout dinâmicos com a propriedade Flexbox.'
        },

        {
            text: 'jQUery',
            desc: 'Biblioteca open source baseada em javascript. Facilidade em comunicar com o DOM. Forte suporte de uma comunidade por trás. Write less, do more!'
        }

    ];

}
/************************************************/
$(document).ready(function () {

    $(window).stellar();

    var links = $('.navigation').find('li');
    slide = $('.slide');
    button = $('.button');
    mywindow = $(window);
    htmlbody = $('html,body');

    slide.waypoint(function (event, direction) {

        dataslide = $(this).attr('data-slide');

        if (direction === 'down') {
            $('.navigation li[data-slide="' + dataslide + '"]').addClass('active').prev().removeClass('active');
        } else {
            $('.navigation li[data-slide="' + dataslide + '"]').addClass('active').next().removeClass('active');
        }

    });

    mywindow.scroll(function () {
        if (mywindow.scrollTop() == 0) {
            $('.navigation li[data-slide="1"]').addClass('active');
            $('.navigation li[data-slide="2"]').removeClass('active');
        }
    });

    function goToByScroll(dataslide) {
        htmlbody.animate({
            scrollTop: $('.slide[data-slide="' + dataslide + '"]').offset().top
        }, 2000, 'easeInOutQuint');
    }

    links.click(function (e) {
        e.preventDefault();
        dataslide = $(this).attr('data-slide');
        goToByScroll(dataslide);
    });

    button.click(function (e) {
        e.preventDefault();
        dataslide = $(this).attr('data-slide');
        goToByScroll(dataslide);

    });

});
