import argparse
from utils.Agent_discuss import DiscussFlowModel, SingleModel
from utils.Function import import_json, save_json, roles_identity_generate
import os


def experiment_discuss_flow(texts, model_name, discuss_config, rq=None):
    roles = ["Role1", "Role2", "Role3", "Reviewer", "Discussion", "Judge"]

    if isinstance(model_name, list):
        models_name = dict(zip(roles, args.model_name))
    elif isinstance(model_name, str):
        models_name = {role: model_name for role in roles}
    else:
        return

    roles_identity = roles_identity_generate(len(models_name) - 3)  # 固定随机数种子生成
    # roles_identity = roles_identity_generate(1)
    # roles_identity = [roles_identity[0] for _ in range(3)]

    datasets = []

    print(f"------------Current Target Dataset------------")
    for _, text in enumerate(texts):
        text.pop("code", None)
        datasets.append(text)

    discuss_flow = DiscussFlowModel(discuss_config, models_name)
    discuss_flow.target_text = str(datasets)

    roles = discuss_flow.agents_init()
    Reviewer, Discussion, Judge = roles[3], roles[4], roles[5]

    roles = roles[:3]
    roles_positionality, roles_init_codebook = discuss_flow.roles_stage(roles, roles_identity, rq=rq)

    for role_id, positionality, role_init_codebook in zip(roles_identity, roles_positionality, roles_init_codebook):
        role_id["positionality"] = positionality
        role_id["init_codebook"] = role_init_codebook["codebook"]

    init_codebook = []
    for role_identity in roles_identity:
        init_codebook.append({"role": role_identity["role"], "codebook": role_identity["init_codebook"]})

    agreed_disagreed_codebook = discuss_flow.codebook_reviewer(Reviewer, init_codebook)
    final_agreed_codebook = discuss_flow.codebook_discussion(Discussion, agreed_disagreed_codebook)
    final_codebook = discuss_flow.codebook_judge(Judge, init_codebook, agreed_disagreed_codebook, final_agreed_codebook,
                                                 rq)

    result = {
        "Role_Team": roles_identity,
        "Agreed_disagreed_codebook": agreed_disagreed_codebook,
        "Final_agreed_codebook": final_agreed_codebook,
        "Final_codebook": final_codebook,
        "current_num_token": {"input_token": discuss_flow.input_token,
                              "output_token": discuss_flow.output_token}
    }
    save_json(f"{args.output_dir}\\discuss_process\\json\\discuss.json", result)


def experiment_baseline1(texts, model_name, SingleLLM_config):
    SingleLLM = SingleModel(SingleLLM_config, model_name)
    agent = SingleLLM.agent_init()
    dataset = []
    for i, text in enumerate(texts):
        text.pop("code", None)
        dataset.append(text)
    SingleLLM.target_text = str(dataset)
    annotate = SingleLLM.baseline1_codebook_generate(agent)
    codebook = {"Codebook": annotate['codebook']}
    save_json(f"{args.output_dir}\\baseline1\\json\\baseline1.json", codebook)
    print(f"Finish !")


def experiment_baseline2(texts, model_name, discuss_config, rq=None):
    discuss = DiscussFlowModel(discuss_config, {"role1": model_name})
    roles_identitys = roles_identity_generate(3)

    for j, roles_identity in enumerate(roles_identitys):
        roles_positionality_cached = None
        roles_identity = [roles_identity]
        for i, text in enumerate(texts):
            print(f"------------Current Target Text {i + args.start_step}------------")
            discuss.target_text = text["data_chunk"]

            roles, _ = discuss.agents_init(False)
            if roles_positionality_cached is None and args.start_step == 0:
                roles_positionality_cached, roles_annotate = discuss.role_stage(roles, roles_identity, rq=rq,
                                                                                one_role=True,
                                                                                roles_positionality=None)
                save_json(f"{args.output_dir}\\baseline2\\role_positionality.json", roles_positionality_cached)
            else:
                if args.start_step > 0:
                    roles_positionality_cached = import_json(
                        f"{args.output_dir}\\baseline2\\role_positionality.json")
                _, roles_annotate = discuss.role_stage(roles, roles_identity, rq=rq, one_role=True,
                                                       roles_positionality=roles_positionality_cached)
            # roles_positionality_cached = import_json(f"{args.output_dir}\discuss_process\json\\roles_positionality.json")
            # _, roles_annotate = discuss.role_stage(roles, roles_identity, rq=rq, one_role=True,
            #                                       roles_positionality=roles_positionality_cached)
            for role_id, positionality in zip(roles_identity, roles_positionality_cached):
                role_id["positionality"] = positionality
            codebook = {"target_text": text["data_chunk"],
                        "Role": roles_identity,
                        "Codebook": roles_annotate}
            save_json(f"{args.output_dir}\\baseline2\\json\\baseline2_role{j + 1}_{i}.json", codebook)
            print(f"Finish !")


# def experiment_baseline3(texts, model_name, SingleLLM_config):
#     SingleLLM = SingleModel(SingleLLM_config, model_name)
#     agent = SingleLLM.agent_init()
#     codebook = []
#     roles_identity = roles_identity_generate(3)  # 固定随机数种子生成
#     for i, text in enumerate(texts):
#         print(f"------------Current Target Text {i + args.start_step}------------")
#         SingleLLM.target_text = text["data_chunk"]
#         annotate = SingleLLM.baseline23_codebook_generate(agent, roles_identity)
#         codebook.append({"target_text": text["data_chunk"],
#                          "Role_Team": roles_identity,
#                          "Codebook": annotate})
#         print(f"Finish !")
#     save_json(f"{args.output_dir}\\baseline3\codebook.json", codebook)


def parse_args():
    parser = argparse.ArgumentParser("", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input-file", type=str,
                        default=r"F:\Work\Debate\PrivousPerspectiveCoder-LM\Data\Scrum-interviews\processed\Scrum.json",
                        help="raw_text Input file path")
    parser.add_argument("-o", "--output-dir", type=str,
                        default=r"F:\Work\Debate\PrivousPerspectiveCoder-LM\Data\Scrum-interviews\gpt-4o_output",
                        help="Codebook and discuss output file dir")
    parser.add_argument("-c", "--config-dir", type=str,
                        default=r"F:\Work\Debate\PrivousPerspectiveCoder-LM\config\config.json",
                        help="config file dir")
    parser.add_argument("-m", "--model-name", type=str, default="gpt-4o", help="Model name")
    # parser.add_argument("-t", "--temperature", type=float, default=0, hewlp="Sampling temperature")

    parser.add_argument("-s", "--start-step", type=float, default=0, help="Data iteration starting step")
    parser.add_argument("-exp", "--experiment-name", type=float, default=0,
                        help="0: discuss, 1: baseline1, 2: baseline2")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    target_texts = import_json(args.input_file)
    target_texts = target_texts[args.start_step:]
    config = import_json(args.config_dir)
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
        os.mkdir(os.path.join(args.output_dir, "baseline1"))
        os.mkdir(os.path.join(args.output_dir, "baseline1", "json"))
        os.mkdir(os.path.join(args.output_dir, "baseline2"))
        os.mkdir(os.path.join(args.output_dir, "baseline2", "json"))
        os.mkdir(os.path.join(args.output_dir, "discuss_process"))
        os.mkdir(os.path.join(args.output_dir, "discuss_process", "json"))

    if args.experiment_name == 0:
        experiment_discuss_flow(target_texts, args.model_name, config)
    elif args.experiment_name == 1:
        experiment_baseline1(target_texts, args.model_name, config)
    elif args.experiment_name == 2:
        experiment_baseline2(target_texts, args.model_name, config)
