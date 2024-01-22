function Landing() {
    return (
        <body>
            <section class="isolate overflow-hidden bg-white px-6 py-36">
                <div class="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20"></div>
                <div class="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center"></div>
                <div class="mx-auto max-w-2xl lg:max-w-4xl">
                    <img class="mx-auto h-12" src="src\assets\react.svg" alt=""></img>
                    <figure class="mt-10">
                        <blockquote class="text-center text-xl font-bold leading-8 text-gray-900 sm:text-5xl sm:leading-9">
                            <h1>Modul.os</h1>
                            <p class="text-2xl font-normal py-8">Organiza tus reuniones</p>
                        </blockquote>
                    </figure>
                </div>
                <div class="mt-1 mx-auto max-w-2xl lg:max-w-4xl">
                    {/*Boton para ir a inicio de sesión o dashboard*/}
                    <div class="flex justify-center">
                        <a href="/login" class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">Iniciar sesión</a>
                    </div>
                </div>
            </section>
        </body>
    )
}

export default Landing;