import os
import glob
import datetime
import sys
import shutil

# Lista de todas as pastas com o formato "_run_output_*"
dir = os.getcwd()
paths = dir + "\\results\\_run_output_*"
output_folders = glob.glob(paths)


# Para cada pasta encontrada
for output_folder in output_folders:
    # Encontre todas as subpastas dentro dela com o formato "forecasting_test_opt_multivar_2023-*"
    subfolders = glob.glob(
        os.path.join(output_folder, "forecasting_test_opt_multivar_2023-*")
    )
    # print(output_folder, "\n", subfolders)

    for sub in subfolders:
        arquivos = os.listdir(sub)
        if len(arquivos) == 1 and os.path.isfile(
            os.path.join(sub, "experiment_infos.log")
        ):
            # log_file = os.path.join(subfolders[0], "experiment_infos.log")
            # log_creation_time = os.path.getctime(
            #     log_file
            # )  # Obtém a data de criação do arquivo .log
            data_hora_obj1 = datetime.datetime.strptime(
                sub.split("\\")[-1], "forecasting_test_opt_multivar_%Y-%m-%d_%H-%M-%S"
            )
            # Para cada outra pasta com o formato "forecasting_test_opt_multivar_2023-*" na pasta atual
            for subfolder in glob.glob(
                os.path.join(output_folder, "forecasting_test_opt_multivar_2023-*")
            ):
                data_hora_obj2 = datetime.datetime.strptime(
                    subfolder.split("\\")[-1],
                    "forecasting_test_opt_multivar_%Y-%m-%d_%H-%M-%S",
                )
                # Se a data de criação da pasta atual for igual ou maior que a data de criação do arquivo .log
                if data_hora_obj2 >= data_hora_obj1:
                    # Exclua a pasta
                    print(data_hora_obj1, "----", data_hora_obj2)
                    shutil.rmtree(subfolder)
            break
    # sys.exit(0)
