import json
from utils.Agent import Agent
from config.model_menu import *
import random

random.seed(3)


class DiscussFlowModel:
    def __init__(self, discuss_config, models_name):
        self.config = discuss_config
        self.models_name = models_name
        self.target_text = ""
        self.input_token = 0
        self.output_token = 0

    def agents_init(self):
        roles = []
        for i, role in enumerate(self.models_name):
            roles.append(
                Agent(
                    model_name=self.models_name[role],
                    name=role,
                    api_key=api_key[self.models_name[role]],
                    base_url=base_url[self.models_name[role]]
                ))

        return roles

    def role_stage(self, role, rq=None):
        # roles init codebook generate
        if rq is not None:
            role.set_meta_prompt(
                self.config["Agents"]["Coder"]["system_non_pos_rq"].replace("{datasets}", self.target_text)
                .replace("{RQ}", rq))
            role.event(self.config["Agents"]["Coder"]["user_non_pos_rq"])
        else:
            role.set_meta_prompt(
                self.config["Agents"]["Coder"]["system_non_pos"].replace("{datasets}", self.target_text))
            role.event(self.config["Agents"]["Coder"]["user_non_pos"])
        role_response = role.ask()
        role.memory(role_response, False, True)
        self.input_token += role.input_token
        self.output_token += role.output_token

        try:
            codebook = json.loads(role_response)
        except Exception:
            codebook = json.loads(eval(role_response.replace('```', "'''").replace('json', '').strip()))
        return codebook

    def roles_stage(self, roles, roles_identity, rq=None):
        init_codebook, roles_positionality, role_prompt = [], [], []

        for i, role in enumerate(roles):
            if rq is not None:
                pos_prompt = self.config["Agents"]["Positionality"]["user_rq"] \
                    .replace("[Research Question]", rq)
            else:
                pos_prompt = self.config["Agents"]["Positionality"]["user"]
            pos_prompt = pos_prompt \
                .replace("[insert]", roles_identity[i]["role"], 1) \
                .replace("[insert]", roles_identity[i]["Intended_Study_Level"], 1) \
                .replace("[insert]", roles_identity[i]["Subject"], 1) \
                .replace("[insert]", roles_identity[i]["Research_Interest"], 1) \
                .replace("[insert]", roles_identity[i]["Dimensions_Source"], 1)
            # roles system
            role.set_meta_prompt(self.config["Agents"]["Positionality"]["system"])

            # roles positionality statement
            role.event(pos_prompt)
            role_response = role.ask()
            roles_positionality.append(role_response)
            role.memory(role_response, False, True)
            self.input_token += role.input_token
            self.output_token += role.output_token

            # roles init codebook generate
            if rq is not None:
                role.set_meta_prompt(
                    self.config["Agents"]["Coder"]["system_rq"].replace("{datasets}", self.target_text)
                    .replace("{positionality statement}", roles_positionality[i]).replace("{RQ}", rq))
                role.event(self.config["Agents"]["Coder"]["user_rq"])
            else:
                role.set_meta_prompt(
                    self.config["Agents"]["Coder"]["system"].replace("{datasets}", self.target_text)
                    .replace("{positionality statement}", roles_positionality[i]))
                role.event(self.config["Agents"]["Coder"]["user"])
            role_response = role.ask()
            role.memory(role_response, False, True)
            self.input_token += role.input_token
            self.output_token += role.output_token
            try:
                parsed = json.loads(role_response)
            except Exception:
                parsed = json.loads(eval(role_response.replace('```', "'''").replace('json', '').strip()))
            init_codebook.append(parsed)

        return roles_positionality, init_codebook

    def codebook_reviewer(self, reviewer, init_codebook):

        reviewer_system = self.config["Agents"]["Reviewer"]["system"]
        reviewer_user = self.config["Agents"]["Reviewer"]["user"].replace("{codebook}", str(init_codebook))

        reviewer.set_meta_prompt(reviewer_system)
        reviewer.event(reviewer_user)
        reviewer_response = reviewer.ask()
        reviewer.memory(reviewer_response, False, True)
        self.input_token += reviewer.input_token
        self.output_token += reviewer.output_token

        try:
            agreed_disagreed_codebook = json.loads(reviewer_response)
        except Exception:
            agreed_disagreed_codebook = json.loads(
                eval(reviewer_response.replace('```', "'''").replace('json', '').strip()))

        return agreed_disagreed_codebook

    def codebook_discussion(self, discussion, agreed_disagreed_codebook):
        discussion_system = self.config["Agents"]["Discussion"]["system"]
        discussion_user = self.config["Agents"]["Discussion"]["user"] \
            .replace("{codebook}", str(agreed_disagreed_codebook))

        discussion.set_meta_prompt(discussion_system)
        discussion.event(discussion_user)
        discussion_response = discussion.ask()
        discussion.memory(discussion_response, False, True)
        self.input_token += discussion.input_token
        self.output_token += discussion.output_token

        try:
            final_agreed_codebook = json.loads(discussion_response)
        except Exception:
            final_agreed_codebook = json.loads(
                eval(discussion_response.replace('```', "'''").replace('json', '').strip()))

        return final_agreed_codebook

    def codebook_judge(self, Judge, init_codebook, agreed_disagreed_codebook, final_agreed_codebook, rq=None):

        if rq is not None:
            Judge_system = self.config["Agents"]["Judge"]["system_rq"]
            Judge_user = self.config["Agents"]["Judge"]["user_rq"] \
                .replace("{init_codebook}", str(init_codebook)) \
                .replace("{reviewer_output}", str(agreed_disagreed_codebook)) \
                .replace("{discussion_output}", str(final_agreed_codebook))
        else:
            Judge_system = self.config["Agents"]["Judge"]["system"]
            Judge_user = self.config["Agents"]["Judge"]["user"] \
                .replace("{init_codebook}", str(init_codebook)) \
                .replace("{reviewer_output}", str(agreed_disagreed_codebook)) \
                .replace("{discussion_output}", str(final_agreed_codebook))

        Judge.set_meta_prompt(Judge_system)
        Judge.event(Judge_user)
        codebook = Judge.ask()
        Judge.memory(codebook, False, True)
        self.input_token += Judge.input_token
        self.output_token += Judge.output_token

        try:
            parsed = json.loads(codebook)
        except Exception:
            parsed = json.loads(eval(codebook.replace('```', "'''").replace('json', '').strip()))

        return parsed


class SingleModel:
    def __init__(self, config, models_name):
        """Create a Discuss Model
        Args:
            discuss_config: discuss prompt and discuss progress design
            models_name: multi Agents(roles and Facilitator) models name,
        """
        self.config = config
        self.models_name = models_name

        self.target_text = ""

    def agent_init(self):
        """
            return: roles and Facilitator Agent.
        """
        agent = Agent(
            model_name=self.models_name,
            name="SingleLLM",
            api_key=api_key[self.models_name],
            base_url=base_url[self.models_name]
        )
        return agent

    def baseline1_codebook_generate(self, agent):
        agent.set_meta_prompt(self.config["system"])
        agent.event(
            self.config["user"].replace("{dataset}", self.target_text))
        reply = agent.ask()
        agent.memory(reply, False)
        reply = json.loads(reply.replace('```', "").replace('json', '').strip())

        return reply
